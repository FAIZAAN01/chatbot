import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

# Define chat rules
chat_rules = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!']),
    (r'how are you', ['I am just a chatbot.', 'I am doing fine.']),
    (r'quit', ['Goodbye!', 'Bye now.']),
]

chatbot = Chat(chat_rules, reflections)

# Streamlit app
st.title("Simple Chatbot")

# User input
user_input = st.text_input("You: ")

# Check if user has entered input
if user_input:
    if user_input.lower() == 'quit':
        st.text("Chatbot: Goodbye!")
    else:
        response = chatbot.respond(user_input)
        st.text(f"Chatbot: {response}")

# Note: You can add more Streamlit components and customize the UI as needed
