import streamlit as st
import PyPDF2
import re
import json

# Extraire PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Questions et réponses
def parse_questions(text):
    question_pattern = re.compile(
        r"Question n°(\d+)\s+(.+?)\n(?:\s*\n)*(a\).*?b\).*?c\).*?)\s*Réponse ([a-c]+)",
        re.DOTALL,
    )
    questions = []
    for match in question_pattern.finditer(text):
        question_id = int(match.group(1))
        question_text = match.group(2).strip()
        options_raw = match.group(3).strip()
        correct_answers = list(match.group(4).strip())

        # Options
        options = dict(re.findall(r"([a-c])\)\s*(.+?)(?=\n[a-c]\)|$)", options_raw))

        questions.append({
            "question_id": question_id,
            "question_text": question_text,
            "options": options,
            "correct_answers": correct_answers,
        })
    return questions

# Streamlit
st.title("Extraction de Questions-Réponses depuis un PDF")
st.write("Chargez un fichier PDF contenant des questions et réponses pour générer un fichier JSON.")

uploaded_file = st.file_uploader("Chargez votre fichier PDF", type="pdf")

if uploaded_file is not None:
    st.write("Fichier chargé avec succès.")
    
    with st.spinner("Extraction du texte depuis le PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)
    
    st.write("Texte extrait du PDF.")
    
    with st.spinner("Analyse des questions et réponses..."):
        questions_data = parse_questions(pdf_text)
    
    st.write(f"Nombre de questions extraites : {len(questions_data)}")
    
    #les 5 premières questions
    st.write("Aperçu des questions :")
    st.json(questions_data[:5])

    # Btn JSON 
    json_data = json.dumps(questions_data, indent=4, ensure_ascii=False)
    st.download_button(
        label="Télécharger le fichier JSON",
        data=json_data,
        file_name="questions_code_route.json",
        mime="application/json",
    )
