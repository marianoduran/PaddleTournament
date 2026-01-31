import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fechas y Resultados", page_icon="📅")

st.title("📅 Fechas y Resultados")

# --- Sección 1: Tabla de posiciones ---
st.header("🏆 Tabla de Posiciones")

# Inicialmente vacía o con datos de prueba
data_posiciones = [
    {"Pareja": "Guillermo Sesarego y Agustin Duran", "PJ": 0, "PG": 0, "PP": 0, "GG": 0, "GP": 0, "Puntos": 0},
    {"Pareja": "Matias Duran y Felipe Sesarego", "PJ": 0, "PG": 0, "PP": 0, "GG": 0, "GP": 0, "Puntos": 0},
    {"Pareja": "Bruno Sesarego y Mariano Duran", "PJ": 0, "PG": 0, "PP": 0, "GG": 0, "GP": 0, "Puntos": 0},
    {"Pareja": "Juan Manuel Duran y Pedro Rosso", "PJ": 0, "PG": 0, "PP": 0, "GG": 0, "GP": 0, "Puntos": 0}
]

df_posiciones = pd.DataFrame(data_posiciones)
st.dataframe(df_posiciones, hide_index=True)

# --- Sección 2: Partidos ---
st.header("🎾 Partidos")

st.markdown("### Próximos Partidos")

# Ejemplo de estructura de partidos
# Se puede mejorar para que sea dinámica o cargar desde un archivo/base de datos
partidos = [
    {"Partido": 1, "Fecha": "31-Ene-2026", "Equipo 1": "Guillermo/Agustin", "Equipo 2": "Matias/Felipe", "Resultado": "-"},
    {"Partido": 2, "Fecha": "31-Ene-2026", "Equipo 1": "Bruno/Mariano", "Equipo 2": "Guillermo/Agustin", "Resultado": "-"},
    {"Partido": 3, "Fecha": "31-Ene-2026", "Equipo 1": "Matias/Felipe", "Equipo 2": "Bruno/Mariano", "Resultado": "-"},
]

df_partidos = pd.DataFrame(partidos)
st.table(df_partidos)
