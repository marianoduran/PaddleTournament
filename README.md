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
-   **Tabla de Posiciones**: A table tracking the standings. Columns:
    -   **Pareja**: Team name.
    -   **PJ**: Matches Played.
    -   **PG**: Matches Won.
    -   **PP**: Matches Lost.
    -   **GG**: Games Won.
    -   **GP**: Games Lost.
    -   **Puntos**: Total Points.
-   **Partidos**: A list of matches with dates set to **31-Ene-2026**.

## Next Steps
-   Update `pages/3_Fechas_y_Resultados.py` to enter real match results.
