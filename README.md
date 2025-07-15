# 🐦 Bird RAG Chat Agent

* This project is a Retrieval-Augmented Generation (RAG) chat application that answers questions about bird species by combining vector-based document retrieval with live queries to the eBird API, Wikipedia, and curated media assets.
* This app uses the LangChain framework to create a chat interface for querying bird-related information.
* It allows users to ask questions about bird traits, sightings, photos, hotspots, checklists, taxonomy, and more.
* The chat history is maintained in the session state, and the agent processes user queries to provide relevant answers.
* The app is designed to be user-friendly and interactive, allowing users to explore bird-related data easily.
* Ensure that the necessary dependencies are installed and the FAISS index is created before running this app.
* The app uses Streamlit for the frontend and LangChain for the backend processing.
* Make sure to set up your environment with the required API keys and database connections for the eBird API and SQLite database.
* The app is structured to handle various bird-related queries and provide accurate responses based on the underlying data.
* It also includes error handling to manage exceptions gracefully and inform users of any issues encountered during processing.
* The chat interface is designed to be intuitive, allowing users to interact with the agent seamlessly.
* The app can be extended with additional features or improvements based on user feedback and requirements.
* The code is modular, making it easy to maintain and update as needed.
* The app is a great tool for bird enthusiasts, researchers, and anyone interested in bird-related information.
* It leverages the power of AI and natural language processing to provide a rich user experience.
* The app is built with scalability in mind, allowing for future enhancements and additional functionalities.
* The use of FAISS for vector storage enables efficient querying and retrieval of bird-related data.

Note: Make sure to run the indexer script first to create the FAISS index before using this app.


#### Built using:
* Streamlit for the frontend
* LangChain + OpenAI for LLM-based reasoning
* FAISS for vector indexing
* eBird & Wikipedia for live bird data

---

## 🗂️ Project Structure

```
├── streamlit_app.py        # Main UI
├── birdchat_agent.py       # RAG-powered chatbot agent
├── bird_media.py           # Bird image/audio retrieval
├── data_loader.py          # Loads vector data and metadata
├── ebird_api.py            # Simple eBird API wrappers
├── ebird_extended.py       # Extra utilities for eBird endpoints
├── indexer.py              # Builds FAISS index from RAG chunks
├── rag_data_prep.py        # Preprocesses bird knowledge files
├── setup_data.py           # Downloads/setup data folders
├── wikipedia_scraper.py    # Retrieves bird text from Wikipedia
├── requirements.txt
└── .env                    # API keys and secrets (not included)
```

---

## 🚀 Getting Started

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/bird_rag_chat_agent.git
   cd bird_rag_chat_agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your `.env` file:**
   Create a `.env` file in the root directory with the following:
   ```
   OPENAI_API_KEY=your_openai_key
   EBIRD_API_TOKEN=your_ebird_key
   ```

4. **Run setup and indexing:**
   ```bash
   python setup_data.py
   python rag_data_prep.py
   python indexer.py
   ```

5. **Launch the app:**
   ```bash
   streamlit run streamlit_app.py
   ```

---

## 📦 Libraries

- openai
- langchain
- langchain-community
- langchain-openai
- faiss-cpu
- sentence-transformers
- pandas
- wikipedia
- streamlit
- python-dotenv
- ebird-api

---

## 📬 Contact

For questions or contributions, open an issue or submit a pull request!

---

## 📜 License

MIT License
