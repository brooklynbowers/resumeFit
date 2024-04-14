import streamlit as st

def skills_resources_page():
    st.title("Resources for Improving Your Skills")
    st.markdown("""
    Explore various resources to enhance your professional skills. From online courses to read materials, find everything you need to advance your career.
    """)

    st.subheader("Online Courses")
    st.markdown("""
    - [Coursera](https://www.coursera.org)
    - [Udemy](https://www.udemy.com)
    - [LinkedIn Learning](https://www.linkedin.com/learning/)
    """)

    st.subheader("Recommended Books")
    st.markdown("""
    - *Thinking, Fast and Slow* by Daniel Kahneman
    - *Lean Startup* by Eric Ries
    - *How to Win Friends and Influence People* by Dale Carnegie
    """)

    st.subheader("Professional Networks")
    st.markdown("""
    - [LinkedIn](https://www.linkedin.com)
    - Find local professional meetup groups in your area
    """)

    st.subheader("Interview Preparation Tools")
    st.markdown("""
    - [Pramp](https://www.pramp.com) for practicing mock interviews
    - [Interviewing.io](https://interviewing.io) for anonymous interview practice
    """)

if __name__ == "__main__":
    skills_resources_page()
