import streamlit as st

# Set up the page title and introduction
st.title('Simple Resume Creator 📝')
st.markdown('Welcome to the Simple Resume Creator. Fill in your details to generate your resume.')

# User personal details input
st.header('Personal Details')
name = st.text_input("Name")
email = st.text_input("Email Address")
linkedin = st.text_input("LinkedIn Profile URL")

# User job interests
st.header('Job Interests')
job_interests = st.text_input("What jobs are you interested in?")

# User skills
st.header('Skills')
skills = st.text_input("List your skills relevant to the job you are interested in.")

# User education
st.header('Education')
education_level = st.text_input("Highest Degree Earned")
graduation_year = st.text_input("Graduation Year")
institution_name = st.text_input("Institution Name")

# User experience
st.header('Professional Experience')
job_title = st.text_input("Job Title")
company_name = st.text_input("Company Name")
years_worked = st.text_input("Years Worked")
job_skills_used = st.text_input("Skills Used in This Job")

# Function to format the resume
def generate_resume(details):
    resume_template = f"""
    **Name:** {details['name']}
    **Email:** {details['email']}
    **LinkedIn:** {details['linkedin']}
    **Interested Positions:** {details['job_interests']}
    **Skills:** {details['skills']}
    **Education:** {details['education_level']}, {details['institution_name']}, {details['graduation_year']}
    **Professional Experience:**
    - **Position:** {details['job_title']}
    - **Company:** {details['company_name']}
    - **Duration:** {details['years_worked']}
    - **Skills Used:** {details['job_skills_used']}
    """
    return resume_template

# Button to generate resume
if st.button('Generate Resume'):
    user_details = {
        'name': name,
        'email': email,
        'linkedin': linkedin,
        'job_interests': job_interests,
        'skills': skills,
        'education_level': education_level,
        'graduation_year': graduation_year,
        'institution_name': institution_name,
        'job_title': job_title,
        'company_name': company_name,
        'years_worked': years_worked,
        'job_skills_used': job_skills_used,
    }

    resume = generate_resume(user_details)
    st.subheader('Your Generated Resume')
    st.write(resume)


