import streamlit as st

# Streamlit App
def main():
    st.title("Text Summary Generation")

    # Input Text Box
    user_input = st.text_input("Enter a news article to summarize:", "")
    
    pickle_files = ["Model1","Model2","Model3"]
    selected_file = st.selectbox("Select the model:", pickle_files)
    # Submit Button
    if st.button("Submit"):
        if user_input:
            reversed_text = user_input[::-1]+selected_file  # Reverse the text
            # st.success(f"summary:")
            st.markdown(
                f"""
                <div style="border: 2px solid grey; padding: 10px; background-color: #83f28f; border-radius: 5px;">
                    <strong>Summary:</strong><br>
                    {reversed_text}
                </div>
                """, 
                unsafe_allow_html=True
            )
        else:
            st.warning("Please enter some text before submitting.")

# Run the app
if __name__ == "__main__":
    main()

