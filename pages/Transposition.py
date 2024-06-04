import streamlit as st
import math

st.set_page_config(
  page_title="Transposition | Kryptos"
)

st.title('Transposition cipher', anchor=False)

tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])

with tab1:
  st.header('Encryption', anchor=False)
  encrypt_text = st.text_area('Input your text', key=1)
  encrypt_key = st.number_input('Insert a key length', min_value=0, step=1, key=2)
  encrypt_button = st.button('Encrypt', type="primary", use_container_width=True)

with tab2:
  st.header('Decryption', anchor=False)
  decrypt_text = st.text_area(label='Input your text', key=3)
  decrypt_key = st.number_input('Insert a key length', min_value=0, step=1, key=4)
  decrypt_button = st.button('Decrypt', type="primary", use_container_width=True)

def encrypt(text, key):
  ciphertext = [''] * key

  for column in range(key):
    currentIndex = column

    while currentIndex < len(text):
      ciphertext[column] += text[currentIndex]

      currentIndex += key

  return ''.join(ciphertext)

def decrypt(text, key):
  numOfColumns = int(math.ceil(len(text) / key))
  numOfRows = key
  numOfShadedBoxes = (numOfColumns * numOfRows) - len(text)
  result = [''] * numOfColumns
  column = 0
  row = 0
  for symbol in text:
    result[column] += symbol
    column += 1
    if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
      column = 0
      row += 1
  return ''.join(result)

if encrypt_button == True:
  st.header('Cipher text', anchor=False)
  st.write(encrypt(encrypt_text, encrypt_key))
elif decrypt_button == True:
  st.header('Plain text', anchor=False)
  st.write(decrypt(decrypt_text, decrypt_key))
