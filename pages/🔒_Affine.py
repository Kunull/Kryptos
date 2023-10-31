import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
  page_title="D|Cipher"
)

st.title('Affine cipher')

selected = option_menu(
  menu_title=None,
  options = ["Encrypt", "Decrypt"],
  icons = ["lock", "unlock"],
  orientation="horizontal"
)

if selected == "Encrypt":
  st.header('Encryption')
  st.text_area(label='Input your text', key=1)
  st.button('Encrypt', type="primary", use_container_width=True)

if selected == "Decrypt":
  st.header('Decryption')
  st.text_area(label='Input your text', key=2)
  st.button('Decrypt', type="primary", use_container_width=True)