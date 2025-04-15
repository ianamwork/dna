import streamlit as st

# Title
st.title("🧬 Gene Editing & Ethics: Project Website")

# Team Members
st.subheader("👥 Team Members")
st.markdown("- Mitra\n- Ian\n- Gabrielle")

# Project Document
st.subheader("📄 Project Document")

# Topic
st.markdown("**Topic:** Gene editing, designer babies, and the ethics behind genetic modification")

# Mission Statement
st.markdown("**Mission Statement:** We’re looking to examine the scientific consensus on genetic editing versus public sentiment.")

# Exploration Plan
st.markdown("**Exploration Plan:** We will be reviewing PubMed articles as well as New York Times articles.")

# Mind Map
st.subheader("🧠 Mind Map")
st.markdown("[Click here to view our mind map on Miro](https://miro.com/app/board/uXjVIL8Njoo=/)")

# Footer or notes (optional)
st.write("This site is built with ❤️ using Streamlit.")


import streamlit as st

# --- Sidebar Navigation ---
st.sidebar.title("🧬 Gene Editing Project")
section = st.sidebar.radio(
    "Navigate to:",
    ["Background Information", "Current Examples", "Ethics", "Future Implications", "Team"]
)

# --- Main Content Based on Selection ---
if section == "Background Information":
    st.title("🔍 Background Information")
    st.markdown("""
    Welcome to our project on **Gene Editing & Ethics**.  
    Our topic explores *designer babies, genetic modification,* and the science behind gene editing.  
    We aim to understand how society perceives this compared to scientific findings.
    
    ---
    **Topic:** Gene editing, designer babies, and the ethics behind genetic modification  
    **Mission Statement:** We’re looking to examine the scientific consensus on genetic editing versus public sentiment  
    **Exploration Plan:** We will be reviewing PubMed articles as well as New York Times articles  
    """)

    st.subheader("🧠 Mind Map")
    st.markdown("[Click here to view our mind map](https://miro.com/app/board/uXjVIL8Njoo=/)")

elif section == "Current Examples":
    st.title("📚 Current Examples")
    st.markdown("""
    - **CRISPR in medicine**: Used for treating genetic disorders like sickle cell disease.
    - **China's gene-edited babies**: In 2018, a scientist claimed to have edited embryos — causing global controversy.
    - **Agriculture**: Gene editing is already transforming crop production and food security.
    """)

elif section == "Ethics":
    st.title("⚖️ Ethics")
    st.markdown("""
    - What ethical lines exist when editing human embryos?
    - Is it acceptable to edit for non-medical traits like intelligence or appearance?
    - Who decides what’s acceptable? Scientists? Governments? Parents?

    Ethical debates involve issues of:
    - **Consent**
    - **Equity**
    - **Access**
    - **Unintended consequences**
    """)

elif section == "Future Implications":
    st.title("🔮 Future Implications")
    st.markdown("""
    - Could gene editing reduce the burden of disease worldwide?
    - Will inequality increase if only some can afford genetic enhancements?
    - Might society shift its definition of “normal” or “desirable” traits?
    
    What kind of world are we editing ourselves into?
    """)

elif section == "Team":
    st.title("👥 Meet the Team")
    st.markdown("""
    **Mitra**  
    - Research and writing

    **Ian**  
    - Technical lead and design

    **Gabrielle**  
    - Curation and ethical analysis

    ---

    Built with ❤️ using Streamlit.
    """)

