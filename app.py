import streamlit as st
from annotated_text import annotated_text

"""
# Annotated text example

Below is an example of how to use the annotated_text function:
"""

annotated_text(
    "This ",
    ("is", "verb", "#8ef"),
    " some ",
    ("annotated", "adj", "#faa"),
    ("text", "noun", "#afa"),
    " for those of ",
    ("you", "pronoun", "#fea"),
    " who ",
    ("like", "verb", "#8ef"),
    " this sort of ",
    ("thing", "noun", "#afa"),
)