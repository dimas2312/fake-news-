import torch
import io

from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load model and processor (only once)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def describe(image_input):
    """
    Takes a PIL.Image or file-like object and returns a caption describing the content.
    """
    if isinstance(image_input, bytes):
        image = Image.open(io.BytesIO(image_input)).convert("RGB")
    elif isinstance(image_input, Image.Image):
        image = image_input.convert("RGB")
    else:
        raise ValueError("Input must be a PIL image or byte stream.")

    # Preprocess the image
    inputs = processor(image, return_tensors="pt").to(device)

    # Generate caption
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=20)

    caption = processor.decode(output[0], skip_special_tokens=True)

    return caption
