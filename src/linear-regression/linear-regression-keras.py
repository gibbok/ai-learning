import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

# Define the model
l0 = Dense(units=1, input_shape=[1])
model = Sequential([l0])
model.compile(optimizer="sgd", loss="mean_squared_error")

# Data
xs = np.array([1, 2, 3, 4, 5, 6], dtype=float)
ys = np.array([3, 4, 5, 6, 7, 8], dtype=float)  # y = x+2

# Training
model.fit(xs, ys, epochs=500)

# Printing prediction and learned weights
print(model.predict([7]))
print("Here is what I learned: {}".format(l0.get_weights()))

# Visualize the model using Matplotlib
plt.figure(figsize=(8, 6))

# Input layer (l0)
plt.scatter(1, 1, color="blue")  # Input node
plt.scatter(3, 1, color="orange")  # Output node
plt.plot([1, 3], [1, 1], color="black")  # Connection between nodes

plt.title("Neural Network Architecture")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.show()
