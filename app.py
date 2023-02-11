import streamlit as st
from gtts import gTTS
from gtts import *
import PyPDF2
from tqdm import tqdm


st.title('Book Translator and Reader')
pdf_file = st.file_uploader("Upload Book PDF", type=["pdf"])

def pdf_to_text(pdf_file):
    whole = ''
    pdfreader= PyPDF2.PdfReader(pdf_file)
    # choice2 = st.sidebar.selectbox("Translated_Language",lang)
    pages=len(pdfreader.pages)
    
    page = st.slider('Give the range of the Pages you want to access',0, pages, (25, 27   ))
    # [start_page,end_page] = input("Enter the start page number give a space and enter end page number").split(" ")
    for num in tqdm(range(int(page[0]),int(page[1]))):
        Page=pdfreader.pages[num]
        text=Page.extract_text()
        
    whole+=text   

    myobj = gTTS(text=text, lang='en',tld='co.in', slow=False) 
 
    myobj.save("test.wav") 
    return "test.wav",text



if pdf_file is not None:

    A,T = pdf_to_text(pdf_file)
    st.write(T)
    st.audio(A)
