import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Estilos básicos de la página
st.set_page_config(page_title="Pista de Baile", page_icon="💃")
st.markdown("<h1 style='text-align: center; color: #174cab;'>Pista de Baile</h1>", unsafe_allow_html=True)

# Parámetros de la pista de baile
rows = st.number_input("Número de filas de la pista de baile:", min_value=1, step=1, value=5)
columns = st.number_input("Número de columnas de la pista de baile:", min_value=1, step=1, value=5)

# Crear patrón de ajedrez blanco y negro
def create_checkerboard(rows, columns):
    checkerboard = np.zeros((rows, columns))
    checkerboard[1::2, ::2] = 1  # Celdas negras (valor 1)
    checkerboard[::2, 1::2] = 1  # Celdas negras (valor 1)
    return checkerboard

checkerboard = create_checkerboard(rows, columns)

# Contar celdas negras y blancas
black_cells = int(np.sum(checkerboard))
white_cells = int(rows * columns - black_cells)

# Calcular "bajadas" y "esquinas"
bajadas = (rows - 2) * 2 + (columns - 2) * 2
esquinas = 8  # Siempre serán 8 porque cada esquina tiene dos caras

# Mostrar los resultados
st.write(f"<h3 style='text-align: center;'>Celdas Negras: {white_cells} | Celdas Blancas: {black_cells}</h3>", unsafe_allow_html=True)
st.write(f"<h3 style='text-align: center;'>Bajadas: {bajadas} | Esquinas: {esquinas}</h3>", unsafe_allow_html=True)

# Dibujar patrón de ajedrez en blanco y negro
fig, ax = plt.subplots()
ax.imshow(checkerboard, cmap="gray", extent=[0, columns, 0, rows])  # Mapa de colores en blanco y negro
ax.set_xticks(np.arange(0, columns + 1, 1))
ax.set_yticks(np.arange(0, rows + 1, 1))
ax.grid(color="black", linestyle="-", linewidth=2)
ax.set_xticklabels([])
ax.set_yticklabels([])

# Agregar puntos en los costados (bajadas) centrados en cada bloque
for i in range(columns):
    if i != 0 and i != columns - 1:
        ax.plot(i + 0.5, 0.5, "o", color="#00BFFF", markersize=10)  # Puntos azules en la parte inferior
        ax.plot(i + 0.5, rows - 0.5, "o", color="#00BFFF", markersize=10)  # Puntos azules en la parte superior

for j in range(rows):
    if j != 0 and j != rows - 1:
        ax.plot(0.5, j + 0.5, "o", color="#00BFFF", markersize=10)  # Puntos azules en el lado izquierdo
        ax.plot(columns - 0.5, j + 0.5, "o", color="#00BFFF", markersize=10)  # Puntos azules en el lado derecho

# Agregar puntos en las esquinas
ax.plot(0.5, 0.5, "o", color="#FF4500", markersize=12)  # Esquina inferior izquierda
ax.plot(columns - 0.5, 0.5, "o", color="#FF4500", markersize=12)  # Esquina inferior derecha
ax.plot(0.5, rows - 0.5, "o", color="#FF4500", markersize=12)  # Esquina superior izquierda
ax.plot(columns - 0.5, rows - 0.5, "o", color="#FF4500", markersize=12)  # Esquina superior derecha

# Añadir borde alrededor del tablero para destacar
plt.gca().spines["top"].set_color("black")
plt.gca().spines["top"].set_linewidth(4)
plt.gca().spines["bottom"].set_color("black")
plt.gca().spines["bottom"].set_linewidth(4)
plt.gca().spines["left"].set_color("black")
plt.gca().spines["left"].set_linewidth(4)
plt.gca().spines["right"].set_color("black")
plt.gca().spines["right"].set_linewidth(4)

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

# Animación simple usando Streamlit
st.markdown(
    """
    <style>
    @keyframes flicker {
        0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {
            opacity: 1;
        }
        20%, 24%, 55% {
            opacity: 0;
        }
    }
    .flicker {
        animation: flicker 1.5s infinite;
        font-size: 1.5em;
        color: #FF69B4;
        text-align: center;
    }
    </style>
    
    """, unsafe_allow_html=True
)
