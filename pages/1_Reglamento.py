import streamlit as st

st.set_page_config(page_title="Reglamento", page_icon="📜")

st.title("📜 Reglamento del Torneo")

st.markdown("""
### 1. Formato de Juego
**Fase de Grupos**: Se jugará bajo la modalidad de "Round Robin" (todos contra todos).

**Eliminatorias**: Los mejores de cada grupo avanzarán a cuadro principal (Oro) o consolación (Plata).

**Calentamiento**: Máximo de 5 minutos en pista antes de iniciar el encuentro.

**Puntualidad**: Superados los 10 minutos de cortesía tras la hora fijada, la pareja ausente perderá el partido por W.O. (6-0 / 6-0).

### 2. Puntuación
**Partidos**: Se disputarán al mejor de 2 sets con Punto de Oro (sin ventajas).

**Tie-break**: En caso de empate 6-6 en cualquier set, se jugará un tie-break a 7 puntos (con diferencia de dos).

**Super Tie-break**: Si hay empate a un set (1-1), el ganador se decidirá mediante un súper tie-break a 10 puntos en lugar de un tercer set completo.

### 3. Faltas y Penalizaciones
**Saque**: El impacto debe ser por debajo de la cintura y ambos pies detrás de la línea de saque.

**Invasión**: No se permite tocar la red con el cuerpo o la pala en ningún momento del punto.

**Pelota en Red**: Si la pelota toca la red tras un saque y cae en el recuadro correspondiente, se considera "Let" (se repite el saque). Si toca la malla metálica tras botar, es falta.

### 4. Código de Conducta
**Fair Play**: Los jugadores son responsables de cantar las bolas de su propio campo. Ante la duda, se recomienda repetir el punto.

**Respeto**: No se tolerarán insultos, lanzamientos de pala o pelotazos intencionados contra el mobiliario o los rivales.

**Vestimenta**: Uso obligatorio de calzado deportivo adecuado (suela espiga o específica de pádel) y ropa deportiva.

### 5. Sistema de Puntuación (Clasificación)
**Para determinar quién pasa a la siguiente fase, se asignarán puntos por partido jugado de la siguiente manera**:

*   **Partido Ganado**: 3 puntos.
*   **Partido Perdido**: 1 punto (incentivo por completar el partido).
*   **W.O. (No presentado)**: 0 puntos para la pareja ausente (y -1 en la diferencia de sets).

**Criterios de Desempate**: Si dos o más parejas terminan empatadas en puntos al finalizar la fase de grupos, se decidirá el orden según:

1.  Enfrentamiento directo entre las parejas empatadas.
2.  Diferencia de sets (sets ganados menos sets perdidos).
3.  Diferencia de juegos (juegos ganados menos juegos perdidos).
4.  Sorteo (si persiste la igualdad absoluta).

---
**Nota del Organizador**: La decisión del juez-árbitro (o comité organizador) será inapelable en caso de conflicto durante el torneo.
""")
