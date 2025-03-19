import gradio as gr
import requests

# Function to send user messages to Flask API
def chat_with_bot(user_message, history=[]):
    response = requests.post("http://127.0.0.1:5000/chat", json={"message": user_message})
    return response.json()["response"]

# Launch the chatbot UI
chatbot = gr.ChatInterface(chat_with_bot, type="messages")
chatbot.launch(share=True)