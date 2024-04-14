import streamlit as st
from openai import OpenAI
import os

# Get your OpenAI API key from environment variables 
api_key = os.getenv("OPENAI_API_KEY")  # Used in production
client = OpenAI(api_key=api_key)

# Cell 2: Title & Description
st.title('Resume Analyzer')
st.markdown('A useful tool to analyze resume skills, experience, and education against a prospective job description.')

# Cell 3: Function to generate text using OpenAI
def compare_resume_to_job_description(resume_text, job_description_text):
    # Check if API key is set
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return

    client = OpenAI(api_key=api_key)
    model = "gpt-3.5-turbo"  # Using the GPT-3.5 model

    
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
            engine="davinci",  # You can change the engine as necessary
            prompt=prompt,
            max_tokens=500,
            temperature=0.5  # A bit of creativity for nuanced comparison
        )
        
        # Extract the response
        comparison_result = response.choices[0].text.strip()
        
        return comparison_result

    except openai.error.OpenAIError as e:
        st.error("Error calling the OpenAI API")
        return None


# Title & Description
st.title('Resume Analyzer')
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


