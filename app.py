import streamlit as st
def load_ocr():
# Use English by default for best compatibility and low memory footprint
return easyocr.Reader(['en'], gpu=False)


reader = load_ocr()


# -------------------------------
# IMAGE UPLOAD
# -------------------------------
st.header("🖼️ Upload an Image")
uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])


extracted_text = ""


if uploaded_file:
st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
with st.spinner("Extracting text..."):
try:
# easyocr.Reader.readtext accepts bytes or numpy array; pass bytes for simplicity
result = reader.readtext(uploaded_file.read(), detail=0)
if result:
extracted_text = "\n".join(result)
st.success("✅ Text successfully extracted!")
st.text_area("📘 Extracted Text", extracted_text, height=200)


# Save extracted text file to outputs
os.makedirs("outputs", exist_ok=True)
filename = f"outputs/ocr_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(filename, "w", encoding="utf-8") as f:
f.write(extracted_text)
st.download_button("💾 Download Extracted Text", data=extracted_text, file_name="ocr_text.txt")
else:
st.warning("⚠️ No text detected in the image.")
except Exception as e:
st.error(f"OCR failed: {e}")


# -------------------------------
# CHATBOT SECTION (rule-based)
# -------------------------------
st.header("💬 Chatbot Assistant")
user_query = st.text_input("Ask something about the extracted text:")


if st.button("Ask"):
if not extracted_text:
st.warning("⚠️ Please upload an image and extract text first!")
elif not user_query.strip():
st.info("💡 Type a question to get started.")
else:
lower_q = user_query.lower()
response = ""


if "what" in lower_q:
response = f"The text mainly says:\n{extracted_text[:250]}..."
elif "who" in lower_q:
response = "I cannot detect persons, only textual data."
elif "hello" in lower_q or "hi" in lower_q:
response = "Hello 👋! Upload an image and I’ll extract text for you."
elif "how" in lower_q:
response = "I use EasyOCR to detect and extract readable text from your image."
else:
response = f"Here’s a part of your text:\n\n{extracted_text[:300]}..."


st.success("🤖 Chatbot Response:")
st.write(response)


# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("Developed by Santhiya © 2025 • Smart OCR and Chatbot System")
