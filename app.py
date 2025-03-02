import streamlit as st
# from frontend.form.form import complete_form
# from frontend.form.signin import sign_in
from form.signin import sign_in
from form.form import complete_form  # Ensure this import is correct
from filling.wordFilling import fillDoc  # Ensure this import is correct
from diseasEng.diseaseEngine import process_diseases
from filling.wordFilling import fillDoc

def main():
    # Set default page if not already set.
    if "page" not in st.session_state:
        st.session_state["page"] = "form"
    
    # Authentication
    if "logged_in" not in st.session_state:
        sign_in()
    elif st.session_state.logged_in:
        # Navigate based on page state.
        if st.session_state.page == "form":
            complete_form()

        elif st.session_state.page == "doc":
            fillDoc()  # This function contains your disease analysis engine.    

        elif st.session_state.page == "disease_analysis":
            process_diseases()  # New function to process diseases and medications

        else:
            st.write("Unknown page state.")


if __name__ == "__main__":
    main()