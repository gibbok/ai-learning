import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense

l0 = Dense(units=1, input_shape=[1])
model = Sequential([l0])
model.compile(optimizer="sgd", loss="mean_squared_error")

xs = np.array([1, 2, 3, 4, 5, 6], dtype=float)
ys = np.array([3, 4, 5, 6, 7, 8], dtype=float)  # y = x+2

model.fit(xs, ys, epochs=500)

print(model.predict([7]))
print("Here is what I learned: {}".format(l0.get_weights()))
