# Multimodal Assistant

A modern, elegant Streamlit app that lets you upload an image, extract text using OCR, and ask questions about the extracted text using a Hugging Face question-answering model.

## Features
- Upload images (JPG, PNG) and preview them instantly
- Extract text from images using Tesseract OCR
- Ask questions about the extracted text using a transformer QA model (deepset/roberta-base-squad2)

## Requirements
- Python 3.8+
- Streamlit
- Pillow
- pytesseract
- huggingface_hub
- Tesseract OCR (system dependency)

## Setup
1. **Clone this repository or copy the files to your project folder.**
2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Install Tesseract OCR:**
   - [Windows installer](https://github.com/UB-Mannheim/tesseract/wiki)
   - [Other platforms](https://tesseract-ocr.github.io/tessdoc/Installation.html)
4. **Set your Hugging Face API token as an environment variable:**
   - On Windows (PowerShell):
     ```powershell
     $env:HF_TOKEN="your_hf_token_here"
     streamlit run app.py
     ```
   - Or set it permanently in your system/user environment variables.

## Usage
1. Run the app:
   ```bash
   streamlit run app.py
   ```
2. Upload an image with text.
3. Review the extracted text.
4. Ask a question about the text and get an answer from the AI model.

## Credits
- Created by Kawthar Zaraket
- Powered by Streamlit, Tesseract OCR, and Hugging Face 🤗

---

For questions or collaboration, connect on [LinkedIn](https://www.linkedin.com/in/kawthar-zaraket/).
