import streamlit as st

st.set_page_config(page_title="Data Sphere Heroes 2025", layout="centered")
st.title("Data Sphere Heroes 2025")
st.subheader("Bienvenue dans votre espace de création de héros et de cartes !")

# Affichage de l'avatar Ready Player Me
st.write("### Votre avatar Ready Player Me")
avatar_url = "https://models.readyplayer.me/691eef18786317131cd43ddf.glb"

st.write("Voici votre avatar en 3D :")
st.markdown(f"""
https://modelviewer.dev/examples/augmented-reality/#model={avatar_url}
</iframe>
""", unsafe_allow_html=True)

# Zone pour uploader des images (optionnel)
st.write("### Importez vos images ou avatars")
uploaded_file = st.file_uploader("Choisissez une image (PNG, JPG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Votre image importée", use_column_width=True)

st.write("---")
st.write("### Contenu à venir :")
st.write("- Génération de cartes type Pokémon")
st.write("- Création de personnages 3D stylisés")
st.write("- Personnalisation avancée")

st.write("---")
