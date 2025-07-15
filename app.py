from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from torchvision import transforms
from PIL import Image
from model import get_model
from utils.labels import class_labels

app = Flask(__name__)
CORS(app)

MODEL_PATH = "model.pth"

# Load Model
model = get_model(num_classes=len(class_labels))
model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.Grayscale(),
    transforms.ToTensor()
])

@app.route("/")
def home():
    return "Vocabulary Classifier API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files['image']
    image = Image.open(file.stream).convert('RGB')
    tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(tensor)
        prediction = torch.argmax(output, dim=1).item()

    label = class_labels[prediction]
    return jsonify({"class_index": prediction, "label": label})

if __name__ == "__main__":
    app.run(debug=True, port=3000)
