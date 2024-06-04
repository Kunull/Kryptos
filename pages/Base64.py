import streamlit as st
import base64

st.set_page_config(
  page_title="Kryptos"
)

st.title('Base64 cipher', anchor=False)

tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])

with tab1:
  st.header('Encryption', anchor=False)
  encrypt_text = st.text_area('Input your text', key=1)
  encrypt_button = st.button('Encrypt', type="primary", use_container_width=True)

with tab2:
  st.header('Decryption', anchor=False)
  decrypt_text = st.text_area(label='Input your text', key=3)
  decrypt_button = st.button('Decrypt', type="primary", use_container_width=True)

def encrypt(text):
  string_bytes = text.encode("ascii")
  encode_bytes = base64.b64encode(string_bytes)
  result = encode_bytes.decode("ascii")
  return result

def decrypt(text):
  string_bytes = text.encode("ascii")
  decode_bytes = base64.b64decode(string_bytes)
  result = decode_bytes.decode("ascii")
  return result

if encrypt_button == True:
  st.header('Cipher text', anchor=False)
  st.write(encrypt(encrypt_text))
elif decrypt_button == True:
  st.header('Plain text', anchor=False)
  st.write(decrypt(decrypt_text))
