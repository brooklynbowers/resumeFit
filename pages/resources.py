import streamlit as st

def skills_resources_page():
    st.title("Resources for Improving Your Skills")
    st.markdown("""
    Explore various resources to enhance your professional skills. From online courses to read materials, find everything you need to advance your career.
    """)

    st.subheader("Online Courses")
    st.markdown('Enhance your professional qualifications with online courses from top universities and industry leaders. These platforms offer courses across a wide range of subjects, helping you acquire both technical and soft skills relevant to your career path.')
    st.markdown("""
    - [Coursera](https://www.coursera.org)
    - [Udemy](https://www.udemy.com)
    - [LinkedIn Learning](https://www.linkedin.com/learning/)
    """)

    st.subheader("Recommended Books")
    st.markdown('Build your knowledge base with these essential reads recommended for any professional. These books cover crucial topics ranging from decision-making and productivity to interpersonal skills and innovation.')
    st.markdown("""
    - *Thinking, Fast and Slow* by Daniel Kahneman
    - *Lean Startup* by Eric Ries
    - *How to Win Friends and Influence People* by Dale Carnegie
    """)

    st.subheader("Professional Networks")
    st.markdown('Networking is key to professional growth. These platforms help you connect with peers and leaders in your industry, find mentors, and discover new career opportunities.')
    st.markdown("""
    - [LinkedIn](https://www.linkedin.com)
    - Find local professional meetup groups in your area
    """)

    st.subheader("Interview Preparation Tools")
    st.markdown('Preparing for interviews can be daunting. Utilize these tools to practice your interview skills, get feedback, and confidently face your next interview.')
    st.markdown("""
    - [Pramp](https://www.pramp.com) for practicing mock interviews
    - [Interviewing.io](https://interviewing.io) for anonymous interview practice
    """)

if __name__ == "__main__":
    skills_resources_page()
