import streamlit as st

# Set up the page title and introduction
st.title('Advanced Resume Creator 📝')
st.markdown('Welcome to the Advanced Resume Creator. Fill in your details to generate your resume, including multiple education and job experiences.')

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
education_entries = st.session_state.get('education_entries', [])
education_entry = {'degree': '', 'institution_name': '', 'graduation_year': ''}
degree = st.text_input("Highest Degree Earned", key="degree")
institution_name = st.text_input("Institution Name", key="institution")
graduation_year = st.text_input("Graduation Year", key="grad_year")

if st.button('Add Another Education'):
    education_entries.append({'degree': degree, 'institution_name': institution_name, 'graduation_year': graduation_year})
    st.session_state.education_entries = education_entries
    st.experimental_rerun()

# User experience
st.header('Professional Experience')
experience_entries = st.session_state.get('experience_entries', [])
experience_entry = {'job_title': '', 'company_name': '', 'years_worked': '', 'job_skills_used': ''}
job_title = st.text_input("Job Title", key="job_title")
company_name = st.text_input("Company Name", key="company")
years_worked = st.text_input("Years Worked", key="years")
job_skills_used = st.text_input("Skills Used in This Job", key="skills")

if st.button('Add Another Job Experience'):
    experience_entries.append({'job_title': job_title, 'company_name': company_name, 'years_worked': years_worked, 'job_skills_used': job_skills_used})
    st.session_state.experience_entries = experience_entries
    st.experimental_rerun()

# Function to format the resume
def generate_resume(details, educations, experiences):
    education_formatted = "\n".join(f"- **Degree:** {edu['degree']}, **Institution:** {edu['institution_name']}, **Year:** {edu['graduation_year']}" for edu in educations)
    experience_formatted = "\n".join(f"- **Job Title:** {exp['job_title']}, **Company:** {exp['company_name']}, **Years:** {exp['years_worked']}, **Skills:** {exp['job_skills_used']}" for exp in experiences)
    
    resume_template = f"""
    **Name:** {details['name']}
    **Email:** {details['email']}
    **LinkedIn:** {details['linkedin']}
    **Interested Positions:** {details['job_interests']}
    **Skills:** {details['skills']}
    **Education:**
    {education_formatted}
    **Professional Experience:**
    {experience_formatted}
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
    }

    resume = generate_resume(user_details, st.session_state.education_entries, st.session_state.experience_entries)
    st.subheader('Your Generated Resume')
    st.write(resume)

