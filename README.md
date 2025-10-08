
# Smart OCR and Chatbot System


A lightweight Streamlit application to extract text from images (OCR) and interact with the extracted text using a simple chatbot. Designed for CPU-only environments.


## Features
- Image upload & OCR (EasyOCR)
- Text preview & download
- Simple rule-based chatbot for Q&A on extracted text
- Export of extracted text files


## Requirements
- Python 3.8+
- pip packages in `requirements.txt`


## Setup
```bash
git clone https://github.com/<your-username>/smart_ocr_chatbot.git
cd smart_ocr_chatbot
python -m venv .venv
source .venv/bin/activate # or .\.venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py
