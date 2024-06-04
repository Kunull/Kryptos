import streamlit as st

st.set_page_config(
  page_title="Caesar | Kryptos"
)

st.title('Caesar cipher', anchor=False)

tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])

with tab1:
  st.header('Encryption', anchor=False)
  encrypt_text = st.text_area('Input your text', key=1)
  encrypt_key = st.number_input('Insert a key length from 1 to 25', min_value=1, max_value=25, step=1, key=2)
  encrypt_button = st.button('Encrypt', type="primary", use_container_width=True)

with tab2:
  st.header('Decryption', anchor=False)
  decrypt_text = st.text_area(label='Input your text', key=3)
  decrypt_key = st.number_input('Insert a key length from 1 to 25', min_value=1, max_value=25, step=1, key=4)
  decrypt_button = st.button('Decrypt', type="primary", use_container_width=True)

def encrypt(text, key):
  result = ''
  for i in range(len(text)):
    char = text[i]
    if (char.isupper()):
      result += chr((ord(char) + key - 65) % 26 + 65)
    elif (char.islower()):
      result += chr((ord(char) + key - 97) % 26 + 97)
    elif char == '':
      result += ''
  return result

def decrypt(text, key):
  result = ''
  for i in range(len(text)):
    char = text[i]
    if (char.isupper()):
      result += chr((ord(char) - key - 65) % 26 + 65)
    elif (char.islower()):
      result += chr((ord(char) - key - 97) % 26 + 97)
    elif char == '':
      result += ''
  return result

if encrypt_button == True:
  st.header('Cipher text', anchor=False)
  st.write(encrypt(encrypt_text, encrypt_key))
elif decrypt_button == True:
  st.header('Plain text', anchor=False)
  st.write(decrypt(decrypt_text, decrypt_key))

