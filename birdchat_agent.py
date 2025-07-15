
from dotenv import load_dotenv
load_dotenv()

import os
from datetime import date
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import OpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory


from indexer import create_faiss_index
from ebird_api import query_ebird
from ebird_extended import *
from bird_media import get_macaulay_photo_url
from wikipedia_scraper import get_bird_description

INDEX_PATH = "faiss_index"
llm = OpenAI(temperature=0.7)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

if os.path.exists(INDEX_PATH):
    print(f"📦 Loading FAISS index from '{INDEX_PATH}'...")
    db = FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
else:
    db = create_faiss_index(embedding=embeddings)

retriever = db.as_retriever()
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

qa = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
)

last_resolved_species = None

def extract_scientific_name(text):
    words = text.strip().split()
    if len(words) >= 2:
        return " ".join(words[-2:])
    return text

def is_photo_request(text):
    return "photo" in text.lower() or "picture" in text.lower() or "what it looks like" in text.lower()

def is_sighting_request(text):
    return any(kw in text.lower() for kw in ["recent sighting", "seen recently", "observed", "last seen", "any sighting", "recently spotted"])

def is_top_birders_request(text):
    return "top" in text.lower() and "bird" in text.lower()

def is_checklist_request(text):
    return "checklist" in text.lower() or "visit" in text.lower()

def is_hotspot_request(text):
    return "hotspot" in text.lower()

def is_taxonomy_request(text):
    return "species code" in text.lower() or "taxonomy" in text.lower()

def answer_query(user_input):
    global last_resolved_species

    rag_result = qa.invoke({"question": user_input})
    answer = rag_result.get("answer", "").strip()

    inferred_species = extract_scientific_name(user_input)
    if len(inferred_species.split()) == 2:
        last_resolved_species = inferred_species

    name_to_use = last_resolved_species
    fallback_parts = []

    # Route to eBird extensions
    if is_sighting_request(user_input) and name_to_use:
        ebird_info = query_ebird(name_to_use)
        if ebird_info:
            fallback_parts.append(ebird_info)

    if is_photo_request(user_input) and name_to_use:
        photo_url = get_macaulay_photo_url(name_to_use)
        if photo_url:
            fallback_parts.append(f"📸 {photo_url}")

    if is_top_birders_request(user_input):
        fallback_parts.append(str(get_region_top_100("US", str(date.today()))))

    if is_checklist_request(user_input):
        fallback_parts.append(str(checklist_visits("US-NY")))

    if is_hotspot_request(user_input):
        fallback_parts.append(str(get_region_hotspots("US-NY", back=3)))

    if is_taxonomy_request(user_input):
        fallback_parts.append(str(get_taxonomy_all()[:5]))

    if not answer and name_to_use:
        wiki = get_bird_description(name_to_use)
        if wiki and "❌" not in wiki and "⚠️" not in wiki:
            fallback_parts.insert(0, wiki)

    final_parts = []
    if answer:
        final_parts.append(answer)
    final_parts.extend(fallback_parts)

    return "\n\n".join(final_parts) if final_parts else "❌ No reliable information found for your query."

if __name__ == "__main__":
    print("🦜 BirdChat Agent ready. Ask me about any bird!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            break
        print("\n" + answer_query(user_input) + "\n")