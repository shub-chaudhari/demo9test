import streamlit as st

# Streamlit App
def main():
    st.title("Simple Streamlit Web App")

    # Input Text Box
    user_input = st.text_input("Enter something:", "")

    # Submit Button
    if st.button("Submit"):
        if user_input:
            st.success(f"You entered: {user_input}")
        else:
            st.warning("Please enter some text before submitting.")

# Run the app
if __name__ == "__main__":
    main()

