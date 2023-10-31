import streamlit as st

st.set_page_config(
  page_title="D|Cipher"
)

st.title('Railfence cipher', anchor=False)

tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])

with tab1:
  st.header('Encryption', anchor=False)
  encrypt_text = st.text_area('Input your text', key=1)
  encrypt_key = st.number_input('Insert a key', key=2)
  encrypt_button = st.button('Encrypt', type="primary", use_container_width=True)

with tab2:
  st.header('Decryption', anchor=False)
  decrypt_text = st.text_area(label='Input your text', key=3)
  decrypt_key = st.number_input('Insert a key', key=4)
  decrypt_button = st.button('Decrypt', type="primary", use_container_width=True)

def encrypt(text, key):
  rail = [['\n' for i in range(len(text))]
    for j in range(key)]
  dir_down = False
  row, col = 0, 0
  for i in range(len(text)):
    if (row == 0) or (row == key - 1):
      dir_down = not dir_down
    rail[row][col] = text[i]
    col += 1
    if dir_down:
      row += 1
    else:
      row -= 1
  result = []
  for i in range(key):
    for j in range(len(text)):
      if rail[i][j] != '\n':
        result.append(rail[i][j])
  result = ''.join(result)
  return result

def decrypt(text, key):
  rail = [['\n' for i in range(len(text))]
    for j in range(key)]
  dir_down = None
  row, col = 0, 0
  for i in range(len(text)):
    if row == 0:
      dir_down = True
    if row == key - 1:
      dir_down = False
    col += 1
    if dir_down:
      row += 1
    else:
      row -= 1
  index = 0
  for i in range(key):
    for j in range(len(text)):
      if ((rail[i][j] == '*') and
        (index < len(text))):
          rail[i][j] = text[index]
          index += 1
  result = []
  row, col = 0, 0
  for i in range(len(text)):
    if row == 0:
      dir_down = True
    elif row == key - 1:
      dir_down = False
    elif (rail[row][col] != '*'):
      result.append(rail[row][col])
      col += 1
    elif dir_down:
      row += 1
    else:
      row -= 1
  result = ''.join(result)
  return result

if encrypt_button == True:
  st.header('Cipher text', anchor=False)
  st.write(encrypt(encrypt_text, encrypt_key))
elif decrypt_button == True:
  st.header('Plain text', anchor=False)
  st.write(decrypt(decrypt_text, decrypt_key))
