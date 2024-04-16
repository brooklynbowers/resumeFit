import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="Resume Creator", layout="wide")

st.title('Advanced Resume Creator 📝')
st.markdown('Welcome to the Advanced Resume Creator. Fill in your details to generate your resume.')

name = st.text_input("Name")
email = st.text_input("Email Address")
linkedin = st.text_input("LinkedIn Profile URL")
job_interests = st.text_input("What jobs are you interested in?")
skills = st.text_area("List your skills relevant to the job you are interested in.")

# Education Section
st.header("Education Details")
num_education = st.session_state.get('num_education', 1)
for i in range(num_education):
    with st.container():
        st.text_input(f"Degree {i+1}", key=f"Degree_{i}")
        st.text_input(f"Institution {i+1}", key=f"Institution_{i}")
        st.text_input(f"Graduation Year {i+1}", key=f"Grad_Year_{i}")
if st.button('Add Another Education'):
    num_education += 1
    st.session_state.num_education = num_education

# Experience Section
st.header("Job Experiences")
num_experience = st.session_state.get('num_experience', 1)
for i in range(num_experience):
    with st.container():
        st.text_input(f"Job Title {i+1}", key=f"Job_Title_{i}")
        st.text_input(f"Company Name {i+1}", key=f"Company_{i}")
        st.text_input(f"Years Worked {i+1}", key=f"Years_{i}")
        st.text_area(f"Skills Used {i+1}", key=f"Skills_{i}")
if st.button('Add Another Job Experience'):
    num_experience += 1
    st.session_state.num_experience = num_experience

# Function to create PDF resume
def create_pdf(details):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Resume", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Name: {details['name']}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {details['email']}", ln=True)
    pdf.cell(200, 10, txt=f"LinkedIn: {details['linkedin']}", ln=True)
    pdf.cell(200, 10, txt=f"Job Interests: {details['job_interests']}", ln=True)
    pdf.cell(200, 10, txt=f"Skills: {details['skills']}", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt="Education:", ln=True)
    for i in range(st.session_state.num_education):
        degree = st.session_state.get(f"Degree_{i}", "")
        institution = st.session_state.get(f"Institution_{i}", "")
        grad_year = st.session_state.get(f"Grad_Year_{i}", "")
        pdf.cell(200, 10, txt=f"- {degree} from {institution}, {grad_year}", ln=True)

    pdf.cell(200, 10, txt="Professional Experience:", ln=True)
    for i in range(st.session_state.num_experience):
        job_title = st.session_state.get(f"Job_Title_{i}", "")
        company = st.session_state.get(f"Company_{i}", "")
        years = st.session_state.get(f"Years_{i}", "")
        skills = st.session_state.get(f"Skills_{i}", "")
        pdf.cell(200, 10, txt=f"- {job_title} at {company}, {years} years. Skills: {skills}", ln=True)

    return pdf.output(dest='S').encode('latin1')

# Generate and download PDF
if st.button('Generate and Download PDF Resume'):
    details = {'name': name, 'email': email, 'linkedin': linkedin, 'job_interests': job_interests, 'skills': skills}
    pdf_data = create_pdf(details)
    st.download_button(label="Download PDF", data=pdf_data, file_name="resume.pdf", mime='application/pdf')
