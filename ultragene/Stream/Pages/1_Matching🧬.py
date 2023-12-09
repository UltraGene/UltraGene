import streamlit as st
import sys

sys.path.append('..')
from andME import andME
from Matching import Matching


# Streamlit App implement
st.title("DNA Matching :dna:")

# File uploader widget
uploaded_file = st.file_uploader("Choose a file", type='txt')
if uploaded_file is not None:
    # Save the file
    with open("23andMe_data.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())
    # st.success("File saved as 23andMe_data.txt")

    # Run the andME function and show success message
    andME()
    # st.success("Data sorted successfully in andME.")

    # Initialize a progress bar
    progress_bar = st.progress(0)

    # Run the Matching function with progress updates
    Matching()

    # Complete the progress bar
    progress_bar.progress(100, "Data matching successfully, please move to next step.")

    st.balloons()

