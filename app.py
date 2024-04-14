import streamlit as st

st.set_page_config(page_title='ResumeFit', page_icon=':briefcase:', layout='wide')

st.title('Welcome to ResumeFit 👋')
st.markdown('Helping you align your resume with your job aspirations!')

# Possibly set up some initial session state variables or app-wide configurations here
# ...

# The main app.py can remain minimal because the content is in separate pages
st.sidebar.markdown('## Navigation')
st.sidebar.info('Use the sidebar to navigate to different pages of the app.')
