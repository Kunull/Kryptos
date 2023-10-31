import streamlit as st

st.set_page_config(
  page_title="D|Cipher"
)

st.title('Caesar cipher')

tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])

with tab1:
  st.header('Encryption')
  st.text_area(label='Input your text', key=1)
  st.button('Encrypt', type="primary", use_container_width=True)

with tab2:
  st.header('Decryption')
  st.text_area(label='Input your text', key=2)
  st.button('Decrypt', type="primary", use_container_width=True)

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
