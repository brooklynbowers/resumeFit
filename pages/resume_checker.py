import streamlit as st
import openai
import os

# Ensure the OpenAI API key is set
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OpenAI API key is not set. Please set it in your environment variables.")
    st.stop()

# Initialize the OpenAI API
def compare_resume_to_job_description(resume_text, job_description_text):
    # Prepare the prompt for the AI
    prompt = f"""
    Resume: {resume_text}
    
    Job Description: {job_description_text}
    
    Compare the resume and the job description. Identify skill gaps and estimate how qualified the individual is for the job. Provide a detailed analysis including the qualification percentage.
    """
    
    try:
        # Call the OpenAI API using the updated method
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Using the specific model
            prompt=prompt,
            max_tokens=500,
            temperature=0,  # Set temperature to 0 for consistency
            stop=["\n"],  # Assuming you want to stop the response at the first newline
            api_key=api_key  # Ensure to pass the API key
        )
        
        # Extract the response
        return response['choices'][0]['text'].strip()

    except Exception as e:  # This will catch any exception
        st.error(f"Error calling the OpenAI API: {e}")
        return None

# Resume Analyzer UI
st.title('Resume Analyzer 🔎📄')
st.markdown('A useful tool to analyze resume skills, experience, and education against a prospective job description.')

# Input fields for resume and job description
resume_text = st.text_area("Paste your resume here:", height=300)
job_description_text = st.text_area("Paste the job description here:", height=300)

# Button to trigger the analysis
if st.button('Analyze Resume'):
    with st.spinner('Analyzing...'):
        result = compare_resume_to_job_description(resume_text, job_description_text)
        if result:
            st.write(result)
