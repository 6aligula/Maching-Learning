import tensorflow as tf
from tensorflow.keras import layers, models

# Crear un modelo simple para probar la GPU
model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(1000,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy')

# Crear datos ficticios para entrenamiento
import numpy as np
x_train = np.random.rand(1000, 1000)
y_train = np.random.randint(0, 10, size=(1000, 10))

# Entrenar el modelo
model.fit(x_train, y_train, epochs=3, batch_size=32)
