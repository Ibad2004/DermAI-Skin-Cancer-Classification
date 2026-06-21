import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image

from class_names import class_names

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# ==========================================
# LOAD MODEL
# ==========================================
def load_model():

    model = models.resnet50(weights=None)

    model.fc = nn.Sequential(
        nn.Dropout(0.5),
        nn.Linear(2048, 7)
    )

    model.load_state_dict(
        torch.load(
            "../models/resnet50_best.pth",
            map_location=device
        )
    )

    model.to(device)
    model.eval()

    return model


# ==========================================
# TEST TRANSFORM
# ==========================================
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# ==========================================
# PREDICTION FUNCTION
# ==========================================
def predict_image(model, image):

    image = image.convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0)

    image = image.to(device)

    with torch.no_grad():

        outputs = model(image)

        probabilities = torch.softmax(outputs, dim=1)

        confidence, predicted = torch.max(probabilities, 1)

    predicted_class = class_names[predicted.item()]
    confidence_score = confidence.item() * 100

    return predicted_class, confidence_score