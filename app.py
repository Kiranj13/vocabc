from flask import Flask, request, jsonify
import torch
from PIL import Image
from model import get_model
from torchvision import transforms
import io

app = Flask(__name__)

# Load the model
model = get_model(num_classes=38)  # Match your actual classes
model.load_state_dict(torch.load("model.pth", map_location="cpu"))
model.eval()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.Grayscale(),
    transforms.ToTensor()
])

@app.route("/", methods=["GET"])
def health():
    return "✅ Flask API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files['image']
    img = Image.open(file.stream)
    img_tensor = transform(img).unsqueeze(0)

    with torch.no_grad():
        output = model(img_tensor)
        predicted_class = torch.argmax(output, dim=1).item()

    return jsonify({"prediction": predicted_class})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
