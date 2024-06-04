import streamlit as st
import base64

st.set_page_config(
  page_title="D|Cipher"
)

st.title('Reverse | Kryptos', anchor=False)

tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])

with tab1:
  st.header('Encryption', anchor=False)
  encrypt_text = st.text_area('Input your text', key=1)
  encrypt_button = st.button('Encrypt', type="primary", use_container_width=True)

with tab2:
  st.header('Decryption', anchor=False)
  decrypt_text = st.text_area(label='Input your text', key=3)
  decrypt_button = st.button('Decrypt', type="primary", use_container_width=True)

def main(text):
  result = ''
  i = len(text) - 1
  while i >= 0:
    result = result + text[i]
    i = i - 1
  return result

if encrypt_button == True:
  st.header('Cipher text', anchor=False)
  st.write(main(encrypt_text))
elif decrypt_button == True:
  st.header('Plain text', anchor=False)
  st.write(main(decrypt_text))

