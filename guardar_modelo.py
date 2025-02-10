# guardar_modelo.py
import pickle
from sklearn.linear_model import LinearRegression
import pandas as pd

# Datos de ejemplo para entrenamiento
X_train = pd.DataFrame({
    'Carat': [0.5, 1.0, 1.5],
    'Cut_Fair': [1, 0, 0],
    'Cut_Good': [0, 1, 0],
    'Cut_Very Good': [0, 0, 1],
    'Color_D': [1, 0, 0],
    'Clarity_IF': [1, 0, 0],
    'Depth': [60, 61, 62],
    'Table': [55, 56, 57]
})

y_train = [500, 1000, 1500]  # Precios de los diamantes

# Crear y entrenar el modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Guardar el modelo entrenado en un archivo
with open("diamond_price_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Modelo guardado correctamente.")