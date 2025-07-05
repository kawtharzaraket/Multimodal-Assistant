
import streamlit as st
from PIL import Image
import pytesseract
from huggingface_hub import InferenceClient
import os


st.set_page_config(page_title="Multimodal Assistant", page_icon="📝", layout="centered")

st.markdown("""
<style>
body, .main, .block-container {
    background: linear-gradient(120deg, #f8fafc 0%, #e0e7ef 100%) !important;
    font-family: 'Segoe UI', 'Roboto', 'Arial', sans-serif;
}
.cv-card {
    background: rgba(255,255,255,0.98);
    border-radius: 22px;
    box-shadow: 0 6px 32px 0 rgba(80,120,200,0.13);
    padding: 2.7rem 2.2rem 2.2rem 2.2rem;
    margin-top: 2.5rem;
    margin-bottom: 2.5rem;
    max-width: 650px;
    margin-left: auto;
    margin-right: auto;
    border: 1.5px solid #e0e7ef;
    position: relative;
}
.profile-img {
    width: 90px;
    height: 90px;
    object-fit: cover;
    border-radius: 50%;
    border: 3px solid #3b82f6;
    margin: -70px auto 1.2rem auto;
    display: block;
    box-shadow: 0 2px 12px 0 rgba(59,130,246,0.10);
}
.step-list li {
    margin-bottom: 0.7em;
    font-size: 1.08em;
}
.step-list li:before {
    content: attr(data-icon);
    font-family: 'Segoe UI Emoji', 'Apple Color Emoji', 'Noto Color Emoji', sans-serif;
    margin-right: 0.7em;
    font-size: 1.2em;
}
.answer-box {
    background: linear-gradient(90deg, #e0eaff 0%, #f8fafc 100%);
    border-radius: 12px;
    padding: 1.1em 1.2em;
    margin-top: 1em;
    font-size: 1.08em;
    color: #1e293b;
    border: 1px solid #cbd5e1;
    box-shadow: 0 2px 8px 0 rgba(59,130,246,0.07);
}
.footer {
    text-align: center;
    color: #64748b;
    font-size: 0.97em;
    margin-top: 2.5rem;
    margin-bottom: 0.5rem;
}
.footer a {
    color: #3b82f6;
    text-decoration: none;
    margin-left: 0.5em;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="cv-card">
    <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=facearea&w=256&h=256&facepad=2" class="profile-img" alt="Profile">
    <h1 style="text-align:center; font-size:2.2rem; margin-bottom:0.5em;">📝 Multimodal Assistant</h1>
    <p style="text-align:center; color:#475569; font-size:1.1rem; margin-bottom:1.5em;">
        <span style="display:inline-block; background:#e0eaff; color:#2563eb; border-radius:8px; padding:0.2em 0.7em; font-weight:600; font-size:1em; margin-bottom:0.5em;">LLM Project</span><br>
        Upload an image, extract its text, and ask questions about it using advanced AI.<br>
        <span style="font-size:0.98em; color:#64748b;">Perfect for document analysis, study, or accessibility.</span>
    </p>
    <ol class="step-list" style="color:#334155; list-style:none; padding-left:0;">
        <li data-icon="📤">Upload a clear image containing text (screenshot, photo, scan, etc).</li>
        <li data-icon="🔎">Wait for the text to be extracted.</li>
        <li data-icon="💬">Ask a question about the extracted text below.</li>
    </ol>
</div>
""", unsafe_allow_html=True)

hf_token = os.environ.get("HF_TOKEN")


uploaded_file = st.file_uploader("Step 1: Upload an image", type=["png", "jpg", "jpeg"])


if not hf_token:
    st.warning("Hugging Face API token not found. Please set the HF_TOKEN environment variable.")


if uploaded_file and hf_token:
    with st.container():
        image = Image.open(uploaded_file)
        st.image(image, caption="Preview of your uploaded image", use_container_width=True)

        st.markdown("---")
        st.subheader("Step 2: Extracted Text (OCR)")
        ocr_text = pytesseract.image_to_string(image)
        if ocr_text.strip():
            st.code(ocr_text, language="markdown")
        else:
            st.info("No text detected in the image. Please try another image.")

        st.markdown("---")
        st.subheader("Step 3: Ask a question about the extracted text")
        question = st.text_input("Type your question here:")
        if question:
            with st.spinner("Thinking..."):
                client = InferenceClient(
                    provider="hf-inference",
                    api_key=hf_token,
                )
                try:
                    answer = client.question_answering(
                        question=question,
                        context=ocr_text,
                        model="deepset/roberta-base-squad2",
                    )
                    st.markdown(f"<div class='answer-box'><b>Answer:</b><br>{answer['answer']}</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Sorry, there was an error: {e}")

st.markdown("""
<div class="footer">
    <hr style="margin-top:2em; margin-bottom:1em;">
    <span>Created by <b>Kawthar Zaraket</b> &middot; Powered by Streamlit, Tesseract OCR, and Hugging Face 🤗</span><br>
    <a href="https://www.linkedin.com/in/kawthar-zaraket/" target="_blank">LinkedIn</a>
</div>
""", unsafe_allow_html=True)
