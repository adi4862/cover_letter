import streamlit as st

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
            st.text('Generated cover letter will be displayed here')


    


if __name__ == '__main__':
    main()
