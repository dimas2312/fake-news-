# 📦 Project Dependencies

Below is a description of the major Python libraries used in this project, including their roles and how they contribute to tasks like image processing, deep learning, and app deployment.

---

## 🖼️ Image Processing

### **opencv-python**
- **Description**: OpenCV (Open Source Computer Vision Library) is a powerful library for image and video processing.
- **Use Cases**:
    - Reading, resizing, and manipulating images.
    - Performing image transformations or preprocessing.
    - Face detection or edge detection.

### **Pillow**
- **Description**: A modern fork of the Python Imaging Library (PIL), used for basic image manipulation.
- **Use Cases**:
    - Opening and converting images (e.g., to RGB).
    - Saving or displaying images.
    - Used internally by many other libraries like `transformers`.

### **piexif**
- **Description**: A lightweight library for reading, modifying, and stripping EXIF metadata from JPEG files.
- **Use Cases**:
    - Removing location or camera metadata.
    - Manipulating or analyzing image metadata for privacy or analysis.

---

## 🧠 Machine Learning & AI

### **transformers**
- **Description**: Hugging Face’s library for working with state-of-the-art transformer models like GPT, BERT, and BLIP.
- **Use Cases**:
    - Generating text (e.g., fake news with GPT-2).
    - Captioning images (e.g., BLIP for generating image descriptions).
    - Using pre-trained models with minimal setup.

### **torch**
- **Description**: PyTorch, a deep learning framework for building and deploying neural networks.
- **Use Cases**:
    - Running models like BLIP.
    - Handling tensors and GPU acceleration.
    - Serving as the backend for many `transformers` models.

### **deepface**
- **Description**: A high-level Python library for face recognition and analysis built on top of OpenCV, TensorFlow, and PyTorch.
- **Use Cases**:
    - Face detection, verification, and analysis (emotion, age, gender).
    - Optional use in enhancing the realism of fake news (e.g., adding character identity).

### **scikit-learn**
- **Description**: A machine learning toolkit for data preprocessing, classification, clustering, etc.
- **Use Cases**:
    - Feature extraction or data manipulation.
    - Supporting auxiliary ML tasks (e.g., clustering similar articles or images).
    - Often used for evaluation metrics or light model training.

---

## 🧪 Utilities

### **tqdm**
- **Description**: A fast, extensible progress bar library.
- **Use Cases**:
    - Visualizing progress during long-running loops or batch processing.
    - Helpful in debugging or training scenarios.

---

## 🌐 Web Application

### **streamlit**
- **Description**: A fast and easy way to create web apps for machine learning and data science.
- **Use Cases**:
    - Creating the user interface for the fake news generator.
    - Uploading images, displaying results, and interacting with models in real time.
    - No frontend coding required (HTML/CSS/JS-free deployment).

---

## 🧩 Summary Table

| Package         | Purpose                                  |
|-----------------|-------------------------------------------|
| `opencv-python` | Image processing and computer vision     |
| `Pillow`        | Basic image loading and manipulation     |
| `piexif`        | Image metadata editing/removal           |
| `transformers`  | NLP and vision models (BLIP, GPT-2)      |
| `torch`         | Deep learning backend (used by models)   |
| `deepface`      | Face recognition and analysis            |
| `scikit-learn`  | Machine learning utilities                |
| `tqdm`          | Progress visualization                   |
| `streamlit`     | Interactive web app interface            |
