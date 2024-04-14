import streamlit as st
import openai
import os

st.set_page_config(page_title='ResumeFit', page_icon=':briefcase:', layout='wide')

st.title('Welcome to ResumeFit 👋')
st.markdown('Helping you align your resume with your job aspirations!')

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OpenAI API key is not set. Please set it in your environment variables.")
else:
    # Initialize the OpenAI client
    client = openai.OpenAI(api_key=api_key)

# Possibly set up some initial session state variables or app-wide configurations here
# ...

# The main app.py can remain minimal because the content is in separate pages
st.sidebar.markdown('## Navigation')
st.sidebar.info('Use the sidebar to navigate to different pages of the app.')
