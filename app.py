import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Data Sphere Heroes 2025", layout="centered")

# Titre principal
st.title("Data Sphere Heroes 2025")
st.subheader("Bienvenue dans votre espace de création de héros et de cartes !")

# Zone pour uploader des images
st.write("### Importez vos images ou avatars")
uploaded_file = st.file_uploader("Choisissez une image (PNG, JPG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Votre image importée", use_column_width=True)

# Placeholder pour contenu futur
st.write("---")
st.write("### Contenu à venir :")
st.write("- Génération de cartes type Pokémon")
st.write("- Création de personnages 3D stylisés")
st.write("- Personnalisation avancée")

# Pied de page
st.write("---")
st.write("© 2025 Data Sphere Heroes - Créé avec Streamlit")