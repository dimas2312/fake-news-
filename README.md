# Fake Global News (FGN) 

Generate fake news articles based on any uploaded image!
This web app uses cutting-edge deep learning models to analyze an image, describe its content, and then generate a suspicious, dramatic news article—all with the click of a button.

### 🚀 Features

* Image-to-caption: Automatic image content analysis with BLIP.
* Fake news generation: Dramatic fake news article creation based on the image description using GPT-2.  
* Fast, easy-to-use web UI with Streamlit.

---
### Requirements

* Python 3.8 or newer
* pip
* streamlit
* transformers
* torch

---
### 📦 Installation
It's HIGHLY recommended to use a virtual environment such as venv.
1. Clone this repository:
```
git clone https://github.com/yourusername/fake-global-news.git
cd fake-global-news
```
2. Create and activate a virtual environment:

On Windows:

```
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:

```
python3 -m venv .venv
source .venv/bin/activate
```

3. Install required modules:
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install streamlit pillow transformers
```

---
### 🛠️ File Overview
* ui.py — Streamlit web UI to upload images and generate fake news.
* image.py — Contains image analysis and description with BLIP.
* text.py — Generates fake news text using GPT-2 and Huggingface Transformers.

```
.
├── ui.py
└── analysis/
    ├── image.py
    └── text.py
```

---
### 🏃 Running the Project
1. Start the Streamlit app:
```
streamlit run ui.py
```
2. In your browser:
   * By default, Streamlit will open a page [here](http://localhost:8501).
   * Click "Browse files" to upload an image.
   * Hit "📰 Generate article" and watch the AI work!
    
---
### ⚙️ Troubleshooting & Tips
* <b>CUDA/CPU</b>: If you want to use GPU (CUDA), install the appropriate version of PyTorch as per the official guide.
* <b>Model Download</b>: The first time you run the app, Huggingface Transformers will download the necessary models (blip-image-captioning-base, gpt2). Ensure you have a stable internet connection.
* <b>Low RAM</b>: GPT-2 may use significant memory. For limited environments (like Colab/old laptops), consider switching to distilgpt2 in text.py for lower RAM usage.
* If you see ModuleNotFoundError, ensure you followed all pip install commands and your environment is properly activated.

---
### 📑 License
For research or educational use only.