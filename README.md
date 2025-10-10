
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
git clone https://github.com/santhiyagithub/smart_ocr_chatbot.git
cd smart_ocr_chatbot
python -m venv .venv
source .venv/bin/activate # or .\.venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py
```


## Usage

- Upload image (png/jpg/jpeg)

- Click Run OCR (app extracts text)

- Ask questions in the chatbot section

## License

This project is released under the MIT License.

## GitHub: Create repo & push (commands)


Run locally in project root (after creating folder and files):


```bash
git init
git add .
git commit -m "Initial commit: Smart OCR Chatbot"
# create repo on GitHub (name: smart-ocr-chatbot) then:
git remote add origin https://github.com/<your-username>/smart-ocr-chatbot.git
git branch -M main
git push -u origin main
```
