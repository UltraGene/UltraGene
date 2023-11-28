import streamlit as st

st.title("DNA Analysis Chat 🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Suggested questions and specific answers
suggested_questions_and_answers = {
    "What does a DNA position indicate in my report?": "DNA positions refer to specific locations on a chromosome, linked to genetic traits or health conditions.",
    "Can you explain what a functional score is?": "A functional score represents the impact of a genetic variant. Lower scores indicate a higher risk of associated health issues.",
    "How should I interpret a low functional score?": "A low functional score may suggest a higher risk for certain conditions. Consult a healthcare professional for an accurate interpretation.",
    "Is it possible to change my DNA functional score?": "Functional scores are based on genetics, which are unchangeable. Lifestyle and environmental factors can influence gene expression.",
    "What should I do if I have a concerning DNA position or score?": "Discuss concerning results with a healthcare professional for guidance and potential next steps."
}

# Keyword-based responses
responses = {
    "hi": "Hi there.",
    "dna": "DNA, or deoxyribonucleic acid, carries your genetic information and can influence various traits and health conditions.",
    "genetics": "Genetics is the study of genes and heredity, playing a key role in understanding health risks and conditions.",
    "gene therapy": "Gene therapy involves modifying genes to treat or prevent disease. It's a rapidly evolving field with many potential applications.",
    "chromosome": "Chromosomes are structures within cells that contain DNA. Humans typically have 23 pairs of chromosomes.",
    "mutation": "A mutation refers to a change in the DNA sequence. Mutations can be harmless, beneficial, or harmful depending on where they occur and their nature.",
    "genetic testing": "Genetic testing analyzes DNA to identify changes or mutations that could indicate a risk for certain diseases or conditions.",
    "heredity": "Heredity is the passing of traits from parents to offspring through genes, influencing characteristics like eye color and risk for certain diseases.",
    "allele": "An allele is a variant form of a gene. Different alleles can result in different traits, even though they occupy the same gene location.",
    "genome": "The genome is the complete set of an organism's DNA, including all of its genes. It contains all the information needed to build and maintain that organism.",
    "epigenetics": "Epigenetics is the study of how behaviors and environment can cause changes that affect the way genes work. Unlike genetic changes, epigenetic changes are reversible.",
    "rna": "RNA, or ribonucleic acid, is a molecule that plays a critical role in coding, decoding, regulation, and expression of genes.",
    "genotype": "The genotype refers to the genetic makeup of an individual organism. It can determine various traits and characteristics.",
    "phenotype": "The phenotype is the set of observable characteristics of an individual resulting from the interaction of their genotype with the environment.",
    "genetic disorder": "A genetic disorder is a disease caused in whole or in part by a change in the DNA sequence away from the normal sequence.",
    "bioinformatics": "Bioinformatics involves the application of computer technology to manage biological information, especially in the field of genetics and genomics.",
    "crispr": "CRISPR is a revolutionary technology that allows scientists to edit genomes with unprecedented precision, efficiency, and flexibility.",
    "cell": "A cell is the smallest unit of life. Cells are the basic building blocks of all living things and contain the organism's genetic material.",
    "mitosis": "Mitosis is a process where a single cell divides into two identical daughter cells (cell division). It's crucial for growth and repair.",
    "meiosis": "Meiosis is a type of cell division that reduces the number of chromosomes in the parent cell by half and produces four gamete cells.",
    "genetic variation": "Genetic variation is the diversity in gene frequencies within a population. This variation contributes to differences within the species."
}

# Function to add chat messages to history
def add_chat_message(role, content):
    st.session_state.messages.append({"role": role, "content": content})

# Function to process user input and generate a response
def process_user_input(user_input):
    # Determine response based on keywords
    assistant_response = "I'm not sure how to respond to that. Can you please provide more details?"
    for keyword, response in responses.items():
        if keyword in user_input.lower():
            assistant_response = response
            break

    # Add user message and assistant response to chat history
    add_chat_message("user", user_input)
    add_chat_message("assistant", assistant_response)

# Display suggested questions
st.markdown("## Suggested Questions")
for question, answer in suggested_questions_and_answers.items():
    if st.button(question):
        add_chat_message("user", question)
        add_chat_message("assistant", answer)

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    process_user_input(prompt)
