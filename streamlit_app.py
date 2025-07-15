import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import streamlit as st
from birdchat_agent import *

st.set_page_config(page_title="🦜 BirdChat", page_icon="🦜", layout="wide")

st.title("🦜 BirdChat Agent")
st.caption("Ask me about bird traits, sightings, photos, hotspots, checklists, taxonomy & more!")

# Initialize session state variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "last_species" not in st.session_state:
    st.session_state.last_species = None

# Chat input
user_input = st.chat_input("Ask me anything about a bird...")

if user_input:
    with st.spinner("Thinking..."):
        try:
            # Call your agent
            answer = answer_query(user_input)

            # Update memory
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("BirdChat", answer))

        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            st.session_state.chat_history.append(("BirdChat", error_msg))

# Show chat history
for role, message in st.session_state.chat_history:
    if role == "You":
        st.chat_message("user").markdown(message)
    else:
        st.chat_message("assistant").markdown(message)

# Show last species if available
if st.session_state.last_species:
    st.markdown(f"**Last species queried:** {st.session_state.last_species}")
# Footer
st.markdown("---")
st.markdown("Made by [Oluwaseun Akinsulire]()")

# Note: Make sure to run the indexer script first to create the FAISS index before using this app.
# This app uses the LangChain framework to create a chat interface for querying bird-related information.
# It allows users to ask questions about bird traits, sightings, photos, hotspots, checklists, taxonomy, and more.
# The chat history is maintained in the session state, and the agent processes user queries to provide relevant answers.
# The app is designed to be user-friendly and interactive, allowing users to explore bird-related data easily.
# Ensure that the necessary dependencies are installed and the FAISS index is created before running this app.
# The app uses Streamlit for the frontend and LangChain for the backend processing.
# Make sure to set up your environment with the required API keys and database connections for the eBird API and SQLite database.
# The app is structured to handle various bird-related queries and provide accurate responses based on the underlying data.
# It also includes error handling to manage exceptions gracefully and inform users of any issues encountered during processing.
# The chat interface is designed to be intuitive, allowing users to interact with the agent seamlessly.
# The app can be extended with additional features or improvements based on user feedback and requirements.
# The code is modular, making it easy to maintain and update as needed.
# The app is a great tool for bird enthusiasts, researchers, and anyone interested in bird-related information.
# It leverages the power of AI and natural language processing to provide a rich user experience.
# The app is built with scalability in mind, allowing for future enhancements and additional functionalities.
# The use of FAISS for vector storage enables efficient querying and retrieval of bird-related data.