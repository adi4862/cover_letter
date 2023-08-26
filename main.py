import streamlit as st
import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

def cover_letter(name, course, college, to, company, position, interest, skills, referance) :
    
    llm = OpenAI(temperature=0.5, verbose=True)

    prompt_template_name = PromptTemplate(
        input_variables= ['name', 'course', 'college', 'to', 'company', 'position', 'interest', 'skills', 'referance'],
        template= '''You are {name} student of{college}. Write a compelling cover letter for a {position} at {company}.
                Highlight your skills as {skills}, you have don't have industrial experiance but have done college project, you have interest in {interest}, show your passion for the job, 
                and explain why you are the ideal candidate for this position. Address the letter to the {to}, if possible, 
                and include a brief introduction, a summary of your qualifications as {course}, you came to know about the opportunity from {referance} and a closing statement expressing your 
                enthusiasm for the opportunity. Your cover letter should be clear, concise, and tailored to the company and job description.'''
    )

    chain = LLMChain(
        llm= llm,
         prompt= prompt_template_name
    )

    cv = chain.run(
        name = name,
        course = course,
        college = college,
        to = to,
        company = company,
        position = position,
        interest = interest,
        skills = skills,
        referance = referance
    )



    return cv.strip()

def main():

    st.title("Generate cover letter ")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Enter the details: ")

        with st.form(key='coverLetter'):
            name = st.text_input("Fullname")
            course = st.text_input('Course')
            college = st.text_input("college")
            to = st.text_input('Recipient')
            company = st.text_input('Company name applying for')
            position = st.text_input('Position')
            interest = st.text_input('Interest')
            skills = st.text_input('Skills')
            referance = st.text_input('Referance')

            submit_button = st.form_submit_button()
            
        # result

        if submit_button:
            st.subheader("Cover letter")
            st.info(cover_letter(name, course, college, to, company, position, interest, skills, referance))


    


if __name__ == '__main__':
    main()
