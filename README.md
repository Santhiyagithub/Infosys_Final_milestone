# 🧠 Smart OCR & Chatbot Assistant  

### 🚀 Project Overview  
The **Smart OCR & Chatbot Assistant** is an intelligent Streamlit-based application that integrates **Optical Character Recognition (OCR)** with an interactive **rule-based chatbot**. The system can extract text from uploaded images using the **EasyOCR** engine and then allow users to query the extracted content through natural language input.  

It simplifies text recognition tasks for images like printed documents, signs, receipts, or handwritten notes, and provides instant chatbot assistance for summarization and context-based responses.  

This project is part of the **Infosys Springboard Virtual Internship 6.0**, developed by *Santhiya & Team* under the mentorship of **Muvendiran M**.  

---

## 📋 Key Features  
✅ **Optical Character Recognition (OCR):**  
Extracts textual data from uploaded images (JPG, PNG, JPEG) using EasyOCR.  

✅ **Intelligent Chatbot:**  
Provides rule-based responses to interpret or summarize extracted text.  

✅ **Interactive Streamlit Interface:**  
A clean, user-friendly dashboard with widgets such as buttons, expanders, text areas, and download options.  

✅ **Downloadable Output:**  
Users can export the extracted text as a `.txt` file for offline reference.  

✅ **Error Handling:**  
Handles cases like empty uploads, unreadable text, and invalid image formats gracefully.  

✅ **Lightweight and Fast:**  
Runs efficiently on CPU without heavy model dependencies — suitable for demo or deployment.  

---

## 🧩 Technology Stack  

| Component | Technology Used |
|------------|-----------------|
| **Frontend** | Streamlit |
| **OCR Engine** | EasyOCR |
| **Language** | Python 3.10+ |
| **Libraries** | `streamlit`, `easyocr`, `os`, `datetime` |
| **File Handling** | Text extraction and download with Streamlit |
| **Storage** | Local `outputs/` directory for saving extracted text |

---

## ⚙️ Installation & Setup  

### Step 1: Clone or Download  
```bash
git clone https://github.com/your-username/smart-ocr-chatbot.git
cd smart-ocr-chatbot
```

### Step 2: Install dependencies
```bash
pip install streamlit easyocr
(if any issues)
pip install torch torchvision torchaudio
```

### Step3: Run the application
```bash
streamlit run app.py
```


## 🖼️ How It Works  

### 🧾 1. Upload Image  
Users upload an image (`JPEG`, `PNG`, or `JPG`) through the Streamlit interface.  

---

### 🔍 2. OCR Extraction  
The **EasyOCR** engine processes the uploaded image and extracts readable text.  
The extracted content is displayed inside a scrollable text area and automatically saved in the local `outputs/` folder with a timestamped filename.  

---

### 💬 3. Chatbot Interaction  
Users can type queries related to the extracted text, such as:  
- “What is written in the image?”  
- “How does this system work?”  
- “Hello / Hi”  

The chatbot then responds contextually using **rule-based logic**, helping users interpret or summarize the text extracted from the image.  

---

### 💾 4. Save Output  
After text extraction, users can **download** the recognized text in `.txt` format using the  
**“💾 Download Extracted Text”** button for offline use.  

---

## 🧠 Rule-Based Chatbot Logic  

| Query Type | Example Input | Response |
|-------------|----------------|-----------|
| **Greeting** | “Hello”, “Hi” | Welcomes the user and explains app functionality |
| **Informational** | “How does it work?” | Describes OCR and EasyOCR process |
| **Contextual** | “What does the image say?” | Displays summarized extracted text |
| **Person-based** | “Who is mentioned?” | States that person recognition isn’t supported |
| **Default** | Any other input | Shows a preview of extracted content |

---

✅ *This logic ensures that even without an LLM or GPU model, the chatbot can deliver quick, meaningful, and rule-based responses to common user queries.*

## 🧰 Project Structure

📦 smart-ocr-chatbot
 ┣ 📂 outputs/                     # Stores extracted OCR text files
 ┣ 📜 app.py                       # Main Streamlit application
 ┣ 📜 requirements.txt             # Dependency list
 ┣ 📜 README.md                    # Documentation
 ┗ 📜 LICENSE                      # MIT License

## 🧪 Example Workflow

1. Run the Streamlit app.
2. Upload an image (e.g., a printed document).
3. Wait for the text extraction to complete.
4. View the extracted content.
5. Ask a question like: “What is in the image?”
6. Download the extracted text if required.

---

## 💡 Future Enhancements

- 🔹 Integrate LLM-based Chatbot (Llama3 or GPT) for deeper context understanding.
- 🔹 Support multi-language OCR (Tamil, Hindi, etc.).
- 🔹 Add image preprocessing filters for noisy or blurred inputs.
- 🔹 Enable PDF text extraction and batch processing.
- 🔹 Implement cloud storage for saving chat and OCR history.

---

## 👨‍💻 Developed By

**Santhiya & Team**  
Batch Number: 1  
Internship Duration: 8 Weeks (08-Sep-2025 → 07-Nov-2025)  
Mentor: Muvendiran M  
Program: Infosys Springboard Virtual Internship 6.0  

---

## 🪪 License

This project is licensed under the **MIT License**.  
You are free to modify and distribute this code for **educational and non-commercial purposes**.
