import streamlit as st
from annotated_text import annotation
from io import StringIO
import json
from service.annotated_words_generator import generate_annotated_words

import html
from htbuilder import H, HtmlElement, a
div = H.div
link = a


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

         args = words
         out = div()

         for arg in args:
             if isinstance(arg, str):
                 out(html.escape(arg))

             elif isinstance(arg, HtmlElement):
                 out(arg)

             elif isinstance(arg, list):
                 wiki_ids = arg[1]
                 if len(wiki_ids) > 0:
                     id = wiki_ids[0]
                     url = "https://www.wikidata.org/wiki/" + id
                     temp = a((annotation(*arg[0])), href=url, target="_blank")
                     out(temp)
                 else:
                     out(annotation(*arg[0]))
             else:
                 raise Exception("Oh noes!")

         st.markdown(str(out), unsafe_allow_html=True)
         st.text("")
