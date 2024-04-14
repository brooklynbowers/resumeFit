import streamlit as st

# Set the page config to set the layout and initial settings of the app
st.set_page_config(page_title='ResumeFit', page_icon=':briefcase:', layout='wide')

# Possibly set up some initial session state variables or app-wide configurations here
# ...

# The main app.py can remain minimal because the content is in separate pages
st.sidebar.markdown('## Navigation')
st.sidebar.info('Use the sidebar to navigate to different pages of the app.')
