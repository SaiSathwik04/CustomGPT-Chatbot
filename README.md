# CustomGPT-Chatbot

## 🚀 Project Description
This project is a **custom chatbot** that can be trained on any text dataset. It provides an interactive conversational experience by leveraging a fine-tuned language model. The chatbot is served via a **Flask API**, and users can interact with it through a **Gradio-based UI**.

## ✨ Features
- 🤖 **Custom GPT-2 Model**: A fine-tuned GPT-2 model that learns from any text data and generates relevant responses.
- 🔗 **Flask API**: A lightweight backend to serve the model and handle requests efficiently.
- 🖥 **Gradio UI**: An easy-to-use graphical interface for user interaction.
- 🏗 **Training Capability**: A Jupyter Notebook (`mini_chatgpt2.ipynb`) is provided for fine-tuning GPT-2 on custom datasets.
- 🛠 **Optimized Model Performance**: Fine-tuned hyperparameters to enhance response quality and coherence.
- 📂 **GitHub-Compatible Paths**: Uses relative paths for seamless collaboration and deployment.
- 🚀 **Future-Proofing**: Designed to be extended with more features and datasets.



## 🤖 Model Training
Training the chatbot model is a crucial phase of the project. To train the GPT-2 model on custom text data, follow these steps:

1. Open `mini_chatgpt2.ipynb` in Jupyter Notebook.
2. Prepare your dataset and update the notebook accordingly.
3. Run the training cells to fine-tune the GPT-2 model.
4. Save the trained model and use it in `app.py` for inference.

## 📦 Installation & Setup
### Prerequisites
Ensure you have Python installed and required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Project
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open the Gradio UI:
   ```bash
   python chat_ui.py
   ```
3. Interact with the chatbot through the web interface.

## 📂 Project Structure
```
gptProject/
│── app.py                   # Flask API for chatbot
│── chat_ui.py               # Gradio-based UI
│── mini_chatgpt2.ipynb      # Jupyter Notebook for training GPT-2
│── requirements.txt         # Dependencies
│── .gitignore               # Git ignore file
│── README.md                # Project documentation
```

## 🚀 Additional Features (Future Work)
- 🏆 Improve model fine-tuning for more accurate responses.
- 📊 Extend training dataset for broader contextual understanding.
- ☁️ Deploy as a cloud-based API for wider accessibility.
- 🛡️ Implement authentication and security measures for production use.

## 📜 License
This project is open-source.

---

Feel free to contribute, suggest improvements, or report issues! 😊

