import streamlit as st
from openai import OpenAI
import os

# Ensure the OpenAI API key is set
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Resume Analyzer UI
st.title('Resume Analyzer 🔎📄')
st.markdown('A useful tool to analyze resume skills, experience, and education against a prospective job description.')

# Initialize the OpenAI API
def compare_resume_to_job_description(resume_text, job_description_text):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return
    
    client = OpenAI(api_key=api_key)
    model = "gpt-3.5-turbo"  # Using the GPT-3.5 model

    # Instructions for the AI (adjust if needed)
    messages = [
        {"role": "system", "content": "You are an assistant who helps individuals identify gaps in their resumes based on job descriptions."},
        {"role": "user", "content": f"Compare the resume and the job description. Identify skill gaps and estimate how qualified the individual is for the job. Provide a detailed analysis including the qualification percentage.\n{resume_text, job_description_text}"}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0  # Lower temperature for less random responses
    )
    return response.choices[0].message.content
    
   

# Input fields for resume and job description
resume_text = st.text_area("Paste your resume here:", height=300)
job_description_text = st.text_area("Paste the job description here:", height=300)

# Button to trigger the analysis
if st.button('Analyze Resume'):
    with st.spinner('Analyzing...'):
        result = compare_resume_to_job_description(resume_text, job_description_text)
        if result:
            st.write(result)



# # Cell 1: Setup
# import streamlit as st
# from openai import OpenAI
# import os

# # Get your OpenAI API key from environment variables 
# api_key = os.getenv("OPENAI_API_KEY")  # Used in production
# client = OpenAI(api_key=api_key)

# # Cell 2: Title & Description
# st.title('Resume Analyzer 🔎📄')
# st.markdown('A useful tool to analyze resume skills, experience, and education against a prospective job description.')

# # Cell 3: Function to generate text using OpenAI
# def analyze_text(text):
#     if not api_key:
#         st.error("OpenAI API key is not set. Please set it in your environment variables.")
#         return
    
#     client = OpenAI(api_key=api_key)
#     model = "gpt-3.5-turbo"  # Using the GPT-3.5 model

#     # Instructions for the AI (adjust if needed)
#     messages = [
#         {"role": "system", "content": "You are an assistant who helps individuals identify gaps in their resumes based on job descriptions."},
#         {"role": "user", "content": f"Compare the resume and the job description. Identify skill gaps and estimate how qualified the individual is for the job. Provide a detailed analysis including the qualification percentage.\n{text}"}
#     ]

#     response = client.chat.completions.create(
#         model=model,
#         messages=messages,
#         temperature=0  # Lower temperature for less random responses
#     )
#     return response.choices[0].message.content


# # Cell 4: Function to generate the image
# def generate_image(text):
#     if not api_key:
#         st.error("OpenAI API key is not set. Please set it in your environment variables.")
#         return

#     response = client.images.generate(
#         model="dall-e-3",
#         prompt=text,
#         size="1024x1024",
#         quality="standard",
#         n=1,
#     )

#     # Assuming the API returns an image URL; adjust based on actual response structure
#     return response.data[0].url

# # Cell 4: Streamlit UI 
# user_input = st.text_area("Enter a brief for your post:", "How should you maintain a deployed model?")

# if st.button('Generate Post Content'):
#     with st.spinner('Generating Text...'):
#         post_text = analyze_text(user_input)
#         st.write(post_text)

#     with st.spinner('Generating Thumbnail...'):
#         thumbnail_url = generate_image(user_input)  # Consider adjusting the prompt for image generation if needed
#         st.image(thumbnail_url, caption='Generated Thumbnail')
