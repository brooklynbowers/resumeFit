import streamlit as st
import os

st.set_page_config(page_title='ResumeFit', page_icon=':briefcase:', layout='wide')

st.title('Welcome to ResumeFit 👋')
st.markdown('We\'re here to guide you through the complexities of the job market. By analyzing your resume and the job descriptions of your interest, ResumeFit identifies the key areas where your qualifications match the job requirements and where you might need improvement. Enhance your resume with tailored advice to not just meet but exceed job expectations. Start your journey to a more fulfilling career today!')

image_url = 'https://raw.githubusercontent.com/brooklynbowers/resumeFit/main/job hunt.jpeg'
st.image(image_url, caption='HR Process - Image courtesy of Pixabay', width=535)


# Possibly set up some initial session state variables or app-wide configurations here
# ...

# The main homepage.py can remain minimal because the content is in separate pages
st.sidebar.markdown('## Navigation')
st.sidebar.info('Use the sidebar to navigate to different pages of the app.')
