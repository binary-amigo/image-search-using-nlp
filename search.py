from transformers import BridgeTowerProcessor, BridgeTowerForImageAndTextRetrieval
from PIL import Image
import torch
import os

# Load model and processor
processor = BridgeTowerProcessor.from_pretrained("BridgeTower/bridgetower-base-itm-mlm")
model = BridgeTowerForImageAndTextRetrieval.from_pretrained("BridgeTower/bridgetower-base-itm-mlm")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Search for the best matching image
def image_search(query, image_dir):
    image_files = [os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.lower().endswith(('jpg', 'jpeg', 'png'))]
    scores = {}

    for img_path in image_files:
        image = Image.open(img_path).convert("RGB")
        encoding = processor(text=query, images=image, return_tensors="pt").to(device)
        outputs = model(**encoding)
        scores[img_path] = outputs.logits[0, 1].item()

    best_match = max(scores, key=scores.get)
    return best_match
