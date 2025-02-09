import streamlit as st

# Streamlit App
def main():
    st.title("Text Summary Generation")

    # Input Text Box
    user_input = st.text_input("Enter something:", "")
    
    pickle_files = ["Model1","Model2","Model3"]
    selected_file = st.selectbox("Select a dictionary file:", pickle_files)
    # Submit Button
    if st.button("Submit"):
        if user_input:
            reversed_text = user_input[::-1]+selected_file  # Reverse the text
            
            st.success("Summary :")
            st.write(f"{reversed_text}")
        else:
            st.warning("Please enter some text before submitting.")

# Run the app
if __name__ == "__main__":
    main()

