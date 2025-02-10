import streamlit as st
import pickle
import pandas as pd

# Título de la app
st.title('Diamond Price Prediction')

# Descripción de la app
st.write('This web app predicts the **Diamond Price** based on various features.')

# Cargar el modelo entrenado (debes tener un modelo previamente entrenado)
with open("C:/Users/jbarreto/Desktop/Diamond/diamond_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# Obtener entradas del usuario para las características del diamante
carat = st.number_input('Carat (Weight of the Diamond)')
cut = st.selectbox('Cut', ['Fair', 'Good', 'Very Good', 'Ideal', 'Excellent'])
color = st.selectbox('Color', ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
clarity = st.selectbox('Clarity', ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'])
depth = st.number_input('Depth')
table = st.number_input('Table')

# Convertir las entradas a formato adecuado para el modelo (one-hot encoding si es necesario)
input_data = pd.DataFrame({
    'Carat': [carat],
    'Cut_Fair': [1 if cut == 'Fair' else 0],
    'Cut_Good': [1 if cut == 'Good' else 0],
    'Cut_Very Good': [1 if cut == 'Very Good' else 0],
    'Cut_Ideal': [1 if cut == 'Ideal' else 0],
    'Cut_Excellent': [1 if cut == 'Excellent' else 0],
    'Color_D': [1 if color == 'D' else 0],
    'Color_E': [1 if color == 'E' else 0],
    'Color_F': [1 if color == 'F' else 0],
    'Color_G': [1 if color == 'G' else 0],
    'Color_H': [1 if color == 'H' else 0],
    'Color_I': [1 if color == 'I' else 0],
    'Color_J': [1 if color == 'J' else 0],
    'Clarity_IF': [1 if clarity == 'IF' else 0],
    'Clarity_VVS1': [1 if clarity == 'VVS1' else 0],
    'Clarity_VVS2': [1 if clarity == 'VVS2' else 0],
    'Clarity_VS1': [1 if clarity == 'VS1' else 0],
    'Clarity_VS2': [1 if clarity == 'VS2' else 0],
    'Clarity_SI1': [1 if clarity == 'SI1' else 0],
    'Clarity_SI2': [1 if clarity == 'SI2' else 0],
    'Clarity_I1': [1 if clarity == 'I1' else 0],
    'Depth': [depth],
    'Table': [table]
})

# Verificar que las columnas de entrada coincidan con las del modelo
model_columns = model.feature_names_in_  # Las columnas utilizadas al entrenar el modelo
input_data = input_data[model_columns]  # Asegurarse de que las columnas coincidan

# Predicción del precio
if st.button('Predict Price'):
    prediction = model.predict(input_data)
    st.write(f'The predicted price of the diamond is: ${prediction[0]:.2f}')
