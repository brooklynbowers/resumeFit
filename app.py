import streamlit as st
import os

st.set_page_config(page_title='ResumeFit', page_icon=':briefcase:', layout='wide')

st.title('Welcome to ResumeFit 👋')
st.markdown('We\'re here to guide you through the complexities of the job market. By analyzing your resume and the job descriptions of your interest, ResumeFit identifies the key areas where your qualifications match the job requirements and where you might need improvement. Enhance your resume with tailored advice to not just meet but exceed job expectations. Start your journey to a more fulfilling career today!')

image_url = 'https://pixabay.com/get/g6b8c4bbb6bcd5ee96361669ce1369a05fb61692044596b93efbb4432174e2a7ce06cd87035b23fc49ee8dd8c9cdd256463298c8c55de56bb4f5e7e2fa7a1c7d2_1280.png'
st.image(image_url, caption='HR Process - Image courtesy of Pixabay', width=535)


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
