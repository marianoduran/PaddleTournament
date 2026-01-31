import streamlit as st

st.set_page_config(
    page_title="Torneo de Padel - 2026",
    page_icon="🎾",
    layout="wide"
)

st.title("🎾 Torneo de Padel - 2026")

st.markdown("""
### Bienvenido al Torneo de Padel

Este es el sitio oficial del torneo. Aquí podrás encontrar toda la información relacionada con el evento, 
incluyendo el reglamento, los participantes, las fechas de los partidos y los resultados.

¡Prepárate para la acción!
""")

st.subheader("📷 Galería de Fotos")
st.write("Revive los mejores momentos del torneo en nuestro álbum de fotos.")
st.link_button("Ver Álbum en Google Photos", "https://photos.app.goo.gl/K1Gsx9gBYjrcMJFR6")
