import os

from flask import Flask, jsonify, request
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)

# Load GPT-2 model once at startup (FAST!)
print("🔥 Loading GPT-2 model...")
MODEL_DIR = os.path.join(os.path.dirname(__file__), "models/final_model")
model = GPT2LMHeadModel.from_pretrained(MODEL_DIR)
tokenizer = GPT2Tokenizer.from_pretrained(MODEL_DIR)
print("✅ GPT-2 model loaded!")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    # Generate GPT-2 response
    inputs = tokenizer(user_message, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=50, temperature=0.7)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
