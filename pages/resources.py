import streamlit as st
from openai import OpenAI
import os

# Get your OpenAI API key from environment variables 
api_key = os.getenv("OPENAI_API_KEY")  # Used in production
client = OpenAI(api_key=api_key)

# Cell 2: Title & Description
st.title('Resume Resources Assistant 🤓')
st.markdown('I will help you level up your skills and land your ✨dream job✨')
st.markdown("""
Explore various resources to enhance your professional skills. From online courses to reading materials, find everything you need to advance your career.
""")

# Cell 3: Function to generate text using OpenAI
def analyze_text(text):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return
    
    client = OpenAI(api_key=api_key)
    model = "gpt-3.5-turbo"  # Using the GPT-3.5 model

    # Instructions for the AI (adjust if needed)
    messages = [
        {"role": "system", "content": "You are an assistant who helps find a variety of resources for individuals looking to level up their skills and land a new job."},
        {"role": "user", "content": f"I want to update my current resume based on the job description. Based on the resume and job descriptions, please recommend the following and explain why they would be beneficial to use or learn: 1. online courses, 2. recommended books, 3. professional networks, 4. interview preperation tools. Give each section as a header with emojis: Online Courses 👩‍🏫🎓, Recommended Books 📚, Professional Networks 👥🌐, Interview Preparation Tools 💼😎. Give 3 to 4 examples of each type of resources and provide links if applicable\n{text}"}
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




# def skills_resources_page():
#     st.title("Resources for Improving Your Skills")
#     st.markdown("""
#     Explore various resources to enhance your professional skills. From online courses to reading materials, find everything you need to advance your career.
#     """)

#     st.subheader("Online Courses 👩‍🏫🎓")
#     st.markdown('Enhance your professional qualifications with online courses from top universities and industry leaders. These platforms offer courses across a wide range of subjects, helping you acquire both technical and soft skills relevant to your career path.')
#     st.markdown("""
#     - [Coursera](https://www.coursera.org)
#     - [Udemy](https://www.udemy.com)
#     - [LinkedIn Learning](https://www.linkedin.com/learning/)
#     """)

#     st.subheader("Recommended Books 📚")
#     st.markdown('Build your knowledge base with these essential reads recommended for any professional. These books cover crucial topics ranging from decision-making and productivity to interpersonal skills and innovation.')
#     st.markdown("""
#     - *Thinking, Fast and Slow* by Daniel Kahneman
#     - *Lean Startup* by Eric Ries
#     - *How to Win Friends and Influence People* by Dale Carnegie
#     """)
# "Recommended Books 📚""Professional Networks 👥🌐""Interview Preparation Tools 💼😎"
#     st.subheader("Professional Networks 👥🌐")
#     st.markdown('Networking is key to professional growth. These platforms help you connect with peers and leaders in your industry, find mentors, and discover new career opportunities.')
#     st.markdown("""
#     - [LinkedIn](https://www.linkedin.com)
#     - Find local professional meetup groups in your area
#     """)

#     st.subheader("Interview Preparation Tools 💼😎")
#     st.markdown('Preparing for interviews can be daunting. Utilize these tools to practice your interview skills, get feedback, and confidently face your next interview.')
#     st.markdown("""
#     - [Pramp](https://www.pramp.com) for practicing mock interviews
#     - [Interviewing.io](https://interviewing.io) for anonymous interview practice
#     """)

# if __name__ == "__main__":
#     skills_resources_page()
