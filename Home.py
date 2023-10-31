import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
  selected = option_menu(
    menu_title=None,
    options = ["Home", "Affine", "Base64", "Caesar", "Railfence", "Reverse"],
    icons = ["house", "shield-lock", "shield-lock", "shield-lock", "shield-lock", "shield-lock"]
  )

st.title('D|Cipher',anchor=False)
st.subheader('Web-based toolkit that uses Python to encrypt and decrypt your text.')

st.divider()

st.write("Made by " "[Kunal Walavalkar](https://kunalwalavalkar.vercel.app)")

# st.text('Made by Kunal Walavalkar.')
# st.button('Personal Website', 'https://kunalwalavalkar.vercel.app',)


# code = '''def hello():
#     print("Hello, Streamlit!")'''
# st.code(code, language='python')