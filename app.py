import streamlit as st
from gtts import gTTS
import PyPDF2
from tqdm import tqdm

# Set title of the app
st.title('Book Reader')

# Allow user to upload a PDF file
pdf_file = st.file_uploader("Upload Book PDF", type=["pdf"])

def pdf_to_text(pdf_file):
    whole = ''
    # Read the PDF file using PyPDF2
    pdfreader= PyPDF2.PdfReader(pdf_file)
    # Get the number of pages in the PDF file
    pages=len(pdfreader.pages)
    
    # Allow user to select a range of pages to extract text from
    page = st.slider('Give the range of the Pages you want to access',0, pages, (25, 27 ))
    page  = st.write("Selected Page range",page)
    # Loop through each page in the range and extract the text using PyPDF2
    for num in tqdm(range(int(page[0]),int(page[1]))):
        Page=pdfreader.pages[num]
        text=Page.extract_text()
        whole += text   

    # Convert the extracted text to speech using gTTS
    myobj = gTTS(text=whole, lang='en',tld='co.in', slow=False) 
    # Save the audio file to disk
    myobj.save("test.wav") 
    # Return the path to the audio file and the extracted text
    return "test.wav",whole

# If a PDF file has been uploaded, extract the text and convert it to speech
if pdf_file is not None:
    audio_path, extracted_text = pdf_to_text(pdf_file)
    # Display the extracted text
    st.write(extracted_text)
    # Allow user to listen to the text as speech
    st.audio(audio_path)
