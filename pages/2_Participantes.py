import streamlit as st
import pandas as pd

st.set_page_config(page_title="Participantes", page_icon="👥")

st.title("👥 Participantes")

st.markdown("A continuación, las parejas que darán todo en la cancha:")

participantes = [
    {"Pareja": "Guillermo Sesarego y Agustin Duran"},
    {"Pareja": "Matias Duran y Felipe Sesarego"},
    {"Pareja": "Bruno Sesarego y Mariano Duran"},
    {"Pareja": "Juan Manuel Duran y Pedro Rosso"}
]

df_participantes = pd.DataFrame(participantes)

st.table(df_participantes)
