import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier

# Generar data aleatoria para el tablero de ajedrez
def generate_data():
    np.random.seed()  # Utilizar una semilla aleatoria en cada ejecución
    rows, cols = 4, 4
    samples_per_square = 15
    data = np.random.rand(rows*cols*samples_per_square, 2) * 10
    # data = np.random.randn(rows*cols*samples_per_square, 2) * 10 + 10  # Media: 5, Desviación estándar: 5
    labels = np.where((data[:, 0] // 2) % 2 == (data[:, 1] // 2) % 2, -1, 1)
    return data, labels

# Función para visualizar el tablero
def plot_board():
    plt.figure(figsize=(6, 6))
    for i in range(rows):
        for j in range(cols):
            color = 'red' if (i+j) % 2 == 0 else 'white'
            plt.fill([i, i+1, i+1, i], [j, j, j+1, j+1], color)
    plt.xlim(0, 4)
    plt.ylim(0, 4)
    plt.xticks(range(4))
    plt.yticks(range(4))
    plt.grid(True, linestyle='--', linewidth=1, color='gray')

# Crear y entrenar el perceptrón multicapa
data, labels = generate_data()
mlp = MLPClassifier(hidden_layer_sizes=(5, 5), max_iter=1000, random_state=42)
mlp.fit(data, labels)

# Visualizar el tablero
rows, cols = 4, 4  # Definir las filas y columnas aquí para que funcione correctamente
plot_board()
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='coolwarm', edgecolors='k', linewidth=1)
plt.title("Tablero de ajedrez con puntos aleatorios clasificados")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
