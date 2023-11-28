import streamlit as st
from PIL import Image

# SidePages
st.set_page_config(
    page_title="Multi page App",
    page_icon=":dna:"
)


st.title("Main page :microscope:")

# Introduction text
st.markdown("""
    **Introduce:**
    Individuals will be able to upload their genetic data to be checked against:
    1. **Functional Data from Multiplex Assays of Variant Effects (MAVEs):** This involves acquiring data through
       Saturation Genome Editing to determine the functional impact of missense genetic variants.
    2. **AlphaMissense In Silico Prediction:** Utilizing AlphaMissense, an in silico prediction tool, to assess 
       the impact of missense variants on VUS, enhancing our understanding of their potential effects.
""")

# Introduction text
st.markdown("""
    **Steps:**
    1. **You will need to upload your 23andMe.txt file in the Matching page(At side bar).**
    2. **Then you will be able to see yor data at Visualize.**
    3. **Also, if there is any issue, chat with the chatbot.**
""")

# Notice text
st.markdown("""
    **_Notice_:warning::**
    
    **In this app we only provide data output, if there is any further inspection. Please, consult your doctor.**
""")

st.sidebar.success("Select a page above.")

# Read in image
image = Image.open('LOGO.png')
st.image(image)

