import os
from flask import Flask, request, jsonify
import torch
from PIL import Image
from model import get_model
from torchvision import transforms

app = Flask(__name__)

# Show current working directory
print("Current working directory:", os.getcwd())

# Update this path based on your real model location
MODEL_PATH = "./model.pth"  # or "models/model.pth", or full path

# Load model safely
try:
    model = get_model(num_classes=38)
    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    model.eval()
except FileNotFoundError:
    print(f"❌ ERROR: Model file not found at '{MODEL_PATH}'")
    exit(1)

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.Grayscale(),
    transforms.ToTensor()
])

@app.route("/", methods=["GET"])
def home():
    return "✅ Flask API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files['image']
    try:
        image = Image.open(file.stream)
    except Exception as e:
        return jsonify({"error": f"Image processing failed: {e}"}), 400

    tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(tensor)
        prediction = torch.argmax(output, dim=1).item()

    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True, port=3000)
