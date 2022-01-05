import streamlit as st
from annotated_text import annotated_text
from io import StringIO
import json
from service.annotated_words_generator import generate_annotated_words


st.header('Text Annotation')
uploaded_file = st.file_uploader("Upload the JSON File", type="json", accept_multiple_files=False)
st.text("")

if uploaded_file is not None:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     string_data = stringio.read()
     json_data = json.loads(string_data)
     sentences = json_data['document']['content']['sentences']

     for sentence in sentences:
         words = generate_annotated_words(sentence)
         annotated_text(*words)
         st.text("")
