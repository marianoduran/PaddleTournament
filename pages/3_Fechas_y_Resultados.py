import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fechas y Resultados", page_icon="📅")

st.title("📅 Fechas y Resultados")

# --- Sección 1: Tabla de posiciones ---
st.header("🏆 Tabla de Posiciones")

import requests
import io

# --- Configuración Google Sheets ---
SHEET_ID = "1Yx_n1_cXS3i8lU1l-9myD39JlygPEI1QeKfojO0rNJw"
SHEET_NAME = "Detalle Partidos"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

@st.cache_data(ttl=60)
def load_data():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(URL, headers=headers)
        response.raise_for_status()
        df = pd.read_csv(io.StringIO(response.text))
        # Seleccionar solo las primeras 5 columnas relevantes
        df = df.iloc[:, :5]
        # Limpiar nombres de columnas
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        st.error(f"Error al cargar datos de Google Sheets: {e}")
        return pd.DataFrame()

# Cargar datos
df_partidos = load_data()

# --- Calcular Tabla de Posiciones ---
st.header("🏆 Tabla de Posiciones")

# Inicializar diccionario de participantes
participantes_nombres = [
    "Guillermo/Agustin",
    "Matias/Felipe",
    "Bruno/Mariano",
    "Juan/Pedro" 
]

# Normalizar nombres para evitar errores de coincidencia
# Se asume que en el sheet los nombres pueden variar ligeramente, pero usaremos los del sheet si existen
if not df_partidos.empty:
    participantes_unicos = set(df_partidos['Pareja Ganadora'].unique()) | set(df_partidos['Pareja perdedora'].unique())
    # Si hay participantes nuevos en el sheet, agrégalos. Si no, usa la lista base.
    if participantes_unicos:
        participantes_nombres = list(participantes_unicos)

tabla = {p: {"PJ": 0, "PG": 0, "PP": 0, "GG": 0, "GP": 0, "Puntos": 0} for p in participantes_nombres}

if not df_partidos.empty:
    for index, row in df_partidos.iterrows():
        ganador = row['Pareja Ganadora']
        perdedor = row['Pareja perdedora']
        games_favor = row['Games a favor']
        games_contra = row['Games en contra']
        
        # Actualizar Ganador
        if ganador in tabla:
            tabla[ganador]["PJ"] += 1
            tabla[ganador]["PG"] += 1
            tabla[ganador]["GG"] += games_favor
            tabla[ganador]["GP"] += games_contra
            tabla[ganador]["Puntos"] += 3
            
        # Actualizar Perdedor
        if perdedor in tabla:
            tabla[perdedor]["PJ"] += 1
            tabla[perdedor]["PP"] += 1
            tabla[perdedor]["GG"] += games_contra # Los games del perdedor son los "en contra" del registro (si asumimos la estructura estándar)
            # REVISIÓN: La columna dice "Games en contra". Si el registro es desde la perspectiva del ganador:
            # Games a favor = Games del Ganador.
            # Games en contra = Games del Perdedor.
            tabla[perdedor]["GP"] += games_favor
            tabla[perdedor]["Puntos"] += 1

# Convertir a DataFrame
data_posiciones = []
for pareja, stats in tabla.items():
    stats["Pareja"] = pareja
    data_posiciones.append(stats)

df_posiciones = pd.DataFrame(data_posiciones)

# Reordenar columnas
df_posiciones = df_posiciones[["Pareja", "PJ", "PG", "PP", "GG", "GP", "Puntos"]]

# Ordenar por Puntos (Descendente), luego diferencia de games (si fuera necesario implementar)
df_posiciones = df_posiciones.sort_values(by="Puntos", ascending=False)

st.dataframe(df_posiciones, hide_index=True)

# --- Sección 2: Partidos ---
st.header("🎾 Partidos")

if not df_partidos.empty:
    st.table(df_partidos)
else:
    st.info("No hay partidos registrados aún.")
