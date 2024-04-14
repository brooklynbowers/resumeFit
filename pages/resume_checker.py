import streamlit as st
import openai 
import os

# Get your OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Ensure that api_key is set before proceeding
if not api_key:
    st.error("OpenAI API key is not set. Please set it in your environment variables.")
    st.stop()

# Function to compare the resume to the job description using OpenAI
def compare_resume_to_job_description(resume_text, job_description_text):
    # Prepare the prompt for the AI
    prompt = f"""
    Compare the following resume with the job description and identify the skill gaps.
    Provide suggestions for improvement and estimate how qualified the individual is for the job, providing a percentage.
    
    Resume:
    {resume_text}

    Job Description:
    {job_description_text}
    """
    
    try:
        # Call the OpenAI API
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=500,
            temperature=0.5,  # A bit of creativity for nuanced comparison
            api_key=api_key  # Pass the API key directly here
        )
        
        # Extract the response
        return response.choices[0].text.strip()

    # except openai.Error as e:  # Corrected exception handling
    #     st.error(f"Error calling the OpenAI API: {e}")
    #     return None

# Resume Analyzer UI
st.title('Resume Analyzer 🔎📄')
st.markdown('A useful tool to analyze resume skills, experience, and education against a prospective job description.')

# Input fields for resume and job description
resume_text = st.text_area("Paste your resume here:", height=300)
job_description_text = st.text_area("Paste the job description here:", height=300)

# Button to trigger the analysis
if st.button('Analyze Resume'):
    with st.spinner('Analyzing...'):
        # Call the function that uses the OpenAI API
        result = compare_resume_to_job_description(resume_text, job_description_text)
        if result:
            st.write(result)
