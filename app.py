import streamlit as st
from string import ascii_letters, digits, punctuation
from random import choices

st.title("Бартків Ділдо Маркет")
lenght = st.slider("длина", 8, 24, 16)
special_characters = st.checkbox("использовать спецсимволи")
if st.button("создать"):
	characters = ascii_letters + digits
	if special_characters:
		characters += punctuation
	password = "".join(choices(characters, k=lenght))
	st.code(password, language="text")
