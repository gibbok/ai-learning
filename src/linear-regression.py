import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense

model = Sequential([Dense(units=1, input_shape=[1])])
model.compile(optimizer="sgd", loss="mean_squared_error")

xs = np.array([1, 2, 3, 4, 5, 6], dtype=float)
ys = np.array([2, 4, 6, 8, 10, 11], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))
