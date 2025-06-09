# 🖼️ Image Captioning Module – `describe.py`
This script defines a function called `describe()` that uses a 
**pretrained BLIP (Bootstrapped Language Image Pretraining)** 
model from Hugging Face to 
**generate a text caption from an input image**.
It uses the **Salesforce BLIP image captioning model** to analyze the image content and return a short textual description.

Imports description: 
 - torch: Handles model loading, tensor computation, and GPU support.
 - io: Used for converting byte input into a stream for PIL.
 - PIL.Image: Handles image file loading and conversion.
 - transformers:
   - BlipProcessor: Prepares images for the BLIP model.
   - BlipForConditionalGeneration: The pretrained BLIP model for generating captions.

---

## 📦 Imports

```python
import torch
import io
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
```

---

## 🧠 Model Initialization

Loads the BLIP base model and processor from Hugging Face. Moves the model to GPU if available, otherwise uses CPU.
This setup is run once to avoid reloading the model multiple times.
```python
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
```

---

## 📝 describe() Function

Accepts either a PIL image or image byte stream. Returns a natural language caption describing the image content.
```python
def describe(image_input):
```

---

## ✅ Input Handling

Supports two input types:
 - Raw bytes (like those from a file upload)
 - PIL.Image instances
Ensures the image is in RGB format.
```python
if isinstance(image_input, bytes):
    image = Image.open(io.BytesIO(image_input)).convert("RGB")
elif isinstance(image_input, Image.Image):
    image = image_input.convert("RGB")
else:
    raise ValueError("Input must be a PIL image or byte stream.")
```

---


## 🔄 Image Processing and Caption Generation
Preprocesses the image for the model using the BLIP processor. Uses the model in inference mode (torch.no_grad()).
Generates a short caption (up to 20 tokens). Decodes the model output into a human-readable string.
```python
inputs = processor(image, return_tensors="pt").to(device)

with torch.no_grad():
    output = model.generate(**inputs, max_new_tokens=20)

caption = processor.decode(output[0], skip_special_tokens=True)
```

---

## 📌 Example Output
If you input an image of a cat sitting on a couch, the output might be:

```text
"A cat sitting on a sofa"
```

