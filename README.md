# Paddle Tournament App - Walkthrough

I have built the Streamlit application for the Paddle Tournament. Here is how you can run it and what you will find.

## How to Run

1.  Open a terminal in the project directory: `/home/marianoduran/Documents/TeamIT-Proyectos/PaddleTournament`
2.  Activate the virtual environment (if not already active):
    ```bash
    source venv/bin/activate
    ```
3.  Run the Streamlit app:
    ```bash
    streamlit run Inicio.py
    ```

## Application Structure

### 🏠 Inicio (`Inicio.py`)
-   Welcome message and tournament description.
-   Button linking to the Google Photos album.

### 📜 Reglamento (`pages/1_Reglamento.py`)
-   Complete tournament rules, including:
    1.  Format of Play
    2.  Scoring
    3.  Fouls and Penalties
    4.  Code of Conduct
    5.  **Scoring System (Classificaton)**: Points per match and tie-breaker criteria.

### 👥 Participantes (`pages/2_Participantes.py`)
-   Displays the list of confirmed couples:
    -   Guillermo Sesarego y Agustin Duran
    -   Matias Duran y Felipe Sesarego
    -   Bruno Sesarego y Mariano Duran
    -   Juan Manuel Duran y Pedro Rosso

### 📅 Fechas y Resultados (`pages/3_Fechas_y_Resultados.py`)
-   **Link to Data**: Direct link to the "Detalle de Partidos" Google Sheet at the top.
-   **Dynamic Integration**: This page now pulls data directly from the Google Sheet.
-   **Tabla de Posiciones**: Automatically calculated from the match results.
    -   Points: 3 for Win, 1 for Loss.
    -   Tracks Matches Played (PJ), Won (PG), Lost (PP), Games Won (GG), Games Lost (GP).
-   **Partidos**: Displays the full list of matches and results fetched from the sheet.

## Next Steps
-   To update the data, simply add new rows to the [Google Sheet](https://docs.google.com/spreadsheets/d/1Yx_n1_cXS3i8lU1l-9myD39JlygPEI1QeKfojO0rNJw/edit?gid=0#gid=0). The app will reflect changes on reload (cached for 60 seconds).
