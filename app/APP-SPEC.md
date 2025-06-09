# 📰 Fake Global News (FGN) – Streamlit App Description

This is a **Streamlit-based web application** that generates a **fake news article** based on an uploaded image. It uses custom analysis modules to describe the image and then generate text content.

---

## 📁 File Overview

```python
import streamlit as st
from analysis.image import describe
from analysis.text import generate
```

## ⚙️ Page Configuration

Sets up the page with a title and centered layout.
Adds a prominent title to the app.
```python
st.set_page_config(page_title="Fake Global News (FGN)", layout="centered")
st.title("Fake News Generator")
```

---

## 🖼️ Image Upload

Prompts the user to upload one image (JPEG or PNG).
Does not allow multiple file uploads.
```python
image_file = st.file_uploader(
    "Load image",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=False,
)
```

---

## 📰 Generate Article Button

Clicking this button triggers the fake news generation process.
```python
if st.button("📰 Generate article"):
```

---

## 🔄 Image Processing & News Generation
Logic analyzing provided image and creating text for new article:
 - Checks if the file is valid and singular.
 - Reads image bytes.
 - Uses describe() to generate a caption or summary of the image.
 - Uses generate() to create a fake news article from that description.
 - Displays the generated article under "🛸 Breaking News 🛸".
 - Provides success, error, or warning feedback.
 - 
```python
if isinstance(image_file, list):
    st.error("Please, load only one image file")
elif image_file is not None:
    image_bytes = image_file.read()

    with st.spinner("Analyzing image..."):
        description = describe(image_bytes)

    news = generate(description)

    st.subheader("🛸 Breaking News 🛸")
    st.write(news)

    st.success("✅ Generating complete!")
else:
    st.warning("Please, load image first!")
```

