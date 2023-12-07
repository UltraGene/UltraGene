import pandas as pd
import streamlit as st


@st.cache_data
def convert_df(df_23DB_selection):
    return df_23DB_selection.to_csv().encode('utf-8')


# Set up the page configuration
st.set_page_config(page_title="Defect DNA dashboard.",
                   page_icon=":bar_chart:",
                   layout="wide")

# Load the data
df_23DB = pd.read_csv("df_23DB.csv")

# Display the title and the full dataframe
st.title(":skull_and_crossbones: 23andMe Matches with MaveDB")
st.dataframe(df_23DB)

CSV = convert_df(df_23DB)

st.download_button(
    label="Download data as CSV",
    data=CSV,
    file_name='23DB',
    mime="text/csv"
)

# ---- SIDEBAR ----
# Sidebar header
st.sidebar.header("Please Filter Here")

# Sidebar multiselect for positions
Position = st.sidebar.multiselect(
    "Select the position:",
    options=df_23DB["position"].unique(),
    default=df_23DB["position"].unique()
)

# ---- MAIN PAGE ----
# Check if at least one position is selected
if not Position:
    # Display a warning message if no position is selected
    st.warning("Please choose at least one position first.")
else:
    # Filter the dataframe based on selected positions
    df_23DB_selection = df_23DB.query("position == @Position")

    # Display the title and the filtered dataframe
    st.title(":eyes: Your selection.")
    st.dataframe(df_23DB_selection)

    CSV = convert_df(df_23DB_selection)

    st.download_button(
        label="Download data as CSV",
        data=CSV,
        file_name='23DB_Selection',
        mime="text/csv"
    )

    # Display overall and average functional scores
    st.title(":bar_chart: Functional Scores for DNA")
    st.markdown("##")

    overall_scores = df_23DB_selection["Functional score"].sum()
    average_score = df_23DB_selection["Functional score"].mean()
    star_rating = ":star:" * int(round(average_score * -10, 0))

    # Layout for displaying scores
    left_column, middle_column = st.columns(2)
    with left_column:
        st.subheader("Overall scores:")
        st.subheader(f"{overall_scores:,}")
    with middle_column:
        st.subheader("Average Functional Scores:")
        st.subheader(f"{average_score} {star_rating}")


# Load the data
common = pd.read_csv("common_positions.csv")

# Common Position
st.title("Matches with AI and  experiment. :laptop:")

# Display Data
st.dataframe(common)

CSV = convert_df(common)

# Download Bottom
st.download_button(
    label="Download data as CSV",
    data=CSV,
    file_name='common_position',
    mime="text/csv"
)


# Outer Link
st.title("More Information: Follow the link  💭")

link = '[Here is the link](https://www.ncbi.nlm.nih.gov/)'
st.markdown(link, unsafe_allow_html=True)