import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Parámetros de la pista de baile
rows = st.number_input("Número de filas de la pista de baile:", min_value=1, step=1)
columns = st.number_input("Número de columnas de la pista de baile:", min_value=1, step=1)

# Crear patrón de ajedrez
def create_checkerboard(rows, columns):
    checkerboard = np.zeros((rows, columns))
    checkerboard[1::2, ::2] = 1  # Celdas negras (valor 1)
    checkerboard[::2, 1::2] = 1  # Celdas negras (valor 1)
    return checkerboard

checkerboard = create_checkerboard(rows, columns)

# Contar celdas negras y blancas
black_cells = np.sum(checkerboard)
white_cells = rows * columns - black_cells

# Mostrar los resultados
st.write(f"Celdas negras: {int(white_cells)}")
st.write(f"Celdas blancas: {int(black_cells)}")

# Dibujar patrón
fig, ax = plt.subplots()
ax.imshow(checkerboard, cmap="gray", extent=[0, columns, 0, rows])
ax.set_xticks(range(columns+1))
ax.set_yticks(range(rows+1))
ax.grid(which="both", color="black", linestyle="-", linewidth=2)
ax.set_xticklabels([])
ax.set_yticklabels([])

# Mostrar en Streamlit
st.pyplot(fig)
