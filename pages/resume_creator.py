import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="Resume Creator", layout="wide")

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
skills = st.text_area("List your skills relevant to the job you are interested in.")

# Section for adding multiple educations
st.header("Education Details")
education_list = st.session_state.get('education_list', [])
degree = st.text_input("Degree")
institution = st.text_input("Institution")
grad_year = st.text_input("Graduation Year")
if st.button('Add Education'):
    education_list.append({'degree': degree, 'institution': institution, 'grad_year': grad_year})
    st.session_state.education_list = education_list
    st.success("Added: {} from {}".format(degree, institution))

# Section for adding multiple job experiences
st.header("Job Experiences")
experience_list = st.session_state.get('experience_list', [])
job_title = st.text_input("Job Title", key="job")
company = st.text_input("Company Name", key="company")
years = st.text_input("Years Worked", key="years")
job_skills = st.text_area("Skills Used", key="skills")
if st.button('Add Job Experience'):
    experience_list.append({'job_title': job_title, 'company': company, 'years': years, 'skills': job_skills})
    st.session_state.experience_list = experience_list
    st.success("Added: {} at {}".format(job_title, company))

# Function to create PDF resume
def create_pdf(details, educations, experiences):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12)
    
    pdf.cell(200, 10, txt="Resume", ln=True, align='C')
    pdf.cell(200, 10, txt="Name: " + details['name'], ln=True)
    pdf.cell(200, 10, txt="Email: " + details['email'], ln=True)
    pdf.cell(200, 10, txt="LinkedIn: " + details['linkedin'], ln=True)
    pdf.cell(200, 10, txt="Job Interests: " + details['job_interests'], ln=True)
    pdf.cell(200, 10, txt="Skills: " + details['skills'], ln=True)
    
    pdf.cell(200, 10, txt="Education:", ln=True)
    for edu in educations:
        pdf.cell(200, 10, txt="- {} at {}, {}".format(edu['degree'], edu['institution'], edu['grad_year']), ln=True)
    
    pdf.cell(200, 10, txt="Professional Experience:", ln=True)
    for exp in experiences:
        pdf.cell(200, 10, txt="- {} at {} ({} years). Skills: {}".format(exp['job_title'], exp['company'], exp['years'], exp['skills']), ln=True)

    return pdf

# Button to generate and download PDF resume
if st.button('Generate and Download PDF Resume'):
    user_details = {
        'name': name,
        'email': email,
        'linkedin': linkedin,
        'job_interests': job_interests,
        'skills': skills,
    }
    pdf = create_pdf(user_details, st.session_state.get('education_list', []), st.session_state.get('experience_list', []))
    pdf.output('resume.pdf')
    with open('resume.pdf', "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="Download PDF", data=PDFbyte, file_name="resume.pdf", mime='application/pdf')

# Display added data for verification
st.subheader("Added Education")
for edu in st.session_state.get('education_list', []):
    st.text(f"{edu['degree']} from {edu['institution']} in {edu['grad_year']}")

st.subheader("Added Job Experiences")
for exp in st.session_state.get('experience_list', []):
    st.text(f"{exp['job_title']} at {exp['company']} for {exp['years']} years. Skills: {exp['skills']}")
