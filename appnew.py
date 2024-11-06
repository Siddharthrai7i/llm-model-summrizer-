from fpdf import FPDF
import streamlit as st
import pickle

st.title("Hello!!! I am A Text Summarizer")

# Load the model within the with block and pass it to the function
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def clean_text(text):
    replacements={
        "\u2018": "'",
        "\u2019": "'",
        "\u201C": '"',
        "\u201D": '"',
        "\u2013": "-",
        "\u2014": "-",
    }
    for original, replacement in replacements.items():
        text= text.replace(original, replacement)
    return text

def create_pdf(summary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True,margin=15)
    pdf.set_font("Arial","B", size=25)
    
    # Add each line of text to the PDF
    pdf.cell(0, 20,"TEXT",  ln=True , align="C")
    
    # Save PDF to a byte stream
    pdf.set_font("Arial" ,size=12)

    cleaned_summary =clean_text(summary)
    pdf.multi_cell(0, 10 , cleaned_summary)
    pdf_data=pdf.output(dest="S")
    return  pdf_data



def predict(text):
    model = load_model()
    prediction = model.predict(text)
    return prediction

input_text = st.text_area("Enter the text you want to summarize:")

if st.button("Summarize"):
    summary = predict(input_text)
    st.write("Summary of your Given text is:")
    st.write(summary)
    st.write("Download options")
    txt_button = st.download_button("Download as TXT", data=summary, file_name="Summary.txt", mime="text/plain")
    pdf_button = st.download_button("Download as PDF", data=create_pdf(summary), file_name="Summary.pdf", mime="application/pdf")
