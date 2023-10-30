import streamlit as st

st.set_page_config(
  page_title="D|Cipher"
)

st.title('Affine cipher')

st.divider()

st.header('Encryption')
st.text_area(label='Input your text', key=1)
st.button('Encrypt', type="primary", use_container_width=True)

st.divider()

st.header('Decryption')
st.text_area(label='Input your text', key=2)
st.button('Decrypt', type="primary", use_container_width=True)