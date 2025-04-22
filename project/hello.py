import streamlit as st

# Title
st.title("🧬 Gene Editing & Ethics: Project Website")
from pathlib import Path
img_path = Path(__file__).parent / "ss1.png"
st.image(str(img_path))

# Team Members
st.subheader("👥 Team Members")
st.markdown("- Mitra\n- Ian\n- Gabrielle")

# Project Document
st.subheader("📄 Project Document")

# Topic
st.markdown("**Topic:** Gene editing, designer babies, and the ethics behind genetic modification")

# Mission Statement
st.markdown("**Mission Statement:** We’re doing an overarching project on CRISPR, looking at current and future implications as well as ethical dilemmas.")

# Exploration Plan
st.markdown("**Exploration Plan:** We will be reviewing PubMed articles as well as New York Times articles.")

st.subheader("Methodology")
st.markdown("We mainly used Google CoLab and chatgpt to conduct a comprehensive search of CRISPR related news and developments from the last couple of years. We provided keywords that our coding used to identify helpful and relevant articles to advance our research. ")
# Mind Map
st.subheader("🧠 Mind Map")
st.markdown("[Click here to view our mind map on Miro](https://miro.com/app/board/uXjVIL8Njoo=/)")

# Footer or notes (optional)


import streamlit as st
from PIL import Image

# --- Sidebar Navigation ---
st.sidebar.title("🧬 Gene Editing Project")
section = st.sidebar.radio(
    "Navigate to:",
    ["Background Information", "Current Examples", "Ethics", "Future Implications", "Team"]
)

# --- Display Logo at the Top ---
logo = Image.open("assets/logo.png")  # Update with your logo file's path
st.image(logo, width=300)
st.markdown(
    f"<div style='text-align: center;'><img src='assets/logo.png' width='300'></div>",
    unsafe_allow_html=True
)




# --- Main Content Based on Selection ---
if section == "Background Information":
    st.title("🔍 Background Information")

  
    st.write("* Target the right gene using engineered guide RNA that matches the sequence to be edited")
    st.write("* Bind the target, where the Cas9 enzyme attaches to the DNA and unwinds it")
    st.write("* Cut the DNA precisely at the intended location")

    st.title("Uses")
    st.write(" Cancer Treatment ⟶  Used CRISPR to identify genes critical to cancer growth and to engineer immune cells that better attack tumors.") 
    st.write("Genetic Diseases ⟶ Promising results in treating diseases like sickle cell anemia and beta thalassemia by reactivating fetal hemoglobin production")
    st.write("Rare Disorders ⟶ CRISPR molecules have been directly injected into patients (e.g., for treating transthyretin amyloidosis) to switch off faulty genes")
    st.write("Agriculture ⟶  Has enabled the creation of crops that produce vitamin D, use less water or fertilizer, are disease-resistant")
    



elif section == "Current Examples":
    st.title("📚 Current Examples")
    st.markdown("""
    - **Covid-19
    - **Sickle Cell
    - **Agriculture**: Gene editing is already transforming crop production and food security.
    - **Fight to Cure Cancer
    """)
    from pathlib import Path
    img_path = Path(__file__).parent / "network.png"
    st.image(str(img_path))
    from pathlib import Path
    img_path = Path(__file__).parent / "gab.png"
    st.image(str(img_path))
    from pathlib import Path
    img_path = Path(__file__).parent / "last.png"
    st.image(str(img_path))
    from pathlib import Path
    img_path = Path(__file__).parent / "jenny.png"
    st.image(str(img_path))
    from pathlib import Path
    img_path = Path(__file__).parent / "nodes.png"
    st.image(str(img_path))
    from pathlib import Path
    img_path = Path(__file__).parent / "newplot.png"
    st.image(str(img_path))

elif section == "Ethics":
    st.title("Ethics")
    st.markdown("""
    - What ethical lines exist when editing human embryos?
    - Is it acceptable to edit for non-medical traits like intelligence or appearance?
    - Who decides what’s acceptable? Scientists? Governments? Parents?

    Ethical debates involve issues of:
    - **Designer Babies**
    - **Affordability**
    - **Misuse**
    """)

elif section == "Future Implications":
    st.title("🔮 Future Implications")
    st.subheader("New Forms")
    st.write("Base editing ⟶ Changes a single letter of DNA wihtout cutting the strand")
    st.write("Prime editing ⟶ More precise 'search-and-replace' capabilites, compared to basic CRISPR")
    st.markdown("""
    - Solving antibiotic resistance
    - helping endangered species 
    - strengthening restrictions and guidelines
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
      """)

