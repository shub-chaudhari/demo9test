import streamlit as st

# Streamlit App
def main():
    st.title("Text Summary Generation")

    # Input Text Box
    user_input = st.text_input("Enter something:", "")

    # Submit Button
    if st.button("Submit"):
        if user_input:
            reversed_text = user_input[::-1]  # Reverse the text
            st.success(f"Reversed Text: {reversed_text}")
        else:
            st.warning("Please enter some text before submitting.")

# Run the app
if __name__ == "__main__":
    main()

