import streamlit as st
from analysis.image import describe
from analysis.text import generate

st.set_page_config(page_title="Fake Global News (FGN)", layout="centered")
st.title("Fake News Generator")

image_file = st.file_uploader(
    "Load image",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=False,
)

if st.button("📰 Generate article"):
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
