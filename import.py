import os
import pickle
from sklearn.linear_model import LinearRegression

# Definir una nueva ruta absoluta
model_path = "C:/Users/jbarreto/Desktop/Diamond/diamond_price_model.pkl"  # Cambié el nombre del archivo por uno diferente

# Crear el directorio donde se guardará el modelo
dir_path = os.path.dirname(model_path)

try:
    os.makedirs(dir_path, exist_ok=True)
    print(f"📁 Directorio creado o ya existente: {dir_path}")
except Exception as e:
    print(f"❌ Error al crear el directorio: {e}")

# Crear un modelo de ejemplo si no existe
model = LinearRegression()

# Guardar el modelo en formato pickle
try:
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print(f"✅ Modelo guardado correctamente en {model_path}")
except Exception as e:
    print(f"❌ Error al guardar el modelo: {e}")