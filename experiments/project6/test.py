# Import the necessary libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Generate some synthetic training data
training_data = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
training_labels = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# Define a simple Keras model
model = Sequential([Dense(units=1, input_shape=[1])])

# Compile the model
model.compile(optimizer="adam", loss="mean_squared_error")

# Train the model (assuming you have training data)
model.fit(training_data, training_labels, epochs=10)

# Convert the Keras model to a TensorFlow Lite model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TensorFlow Lite model to a file
with open("model.tflite", "wb") as f:
    f.write(tflite_model)
