# https://www.tensorflow.org/tutorials/images/classification
import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import pathlib
import matplotlib.pyplot as plt

img_height = 180
img_width = 180

img_path = "./experiments/project6/predict/2.jpg"

img = tf.keras.utils.load_img(
    img_path,
    target_size=(img_height, img_width),
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create a batch

model = keras.models.load_model("./experiments/project6/model.keras")

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])


# Given labels, calculate percentages
flowers = ["daisy", "dandelion", "roses", "sunflowers", "tulips"]

# Pair each flower with its corresponding value
flower_value_pairs = list(zip(flowers, predictions[0]))

sorted_flower_value_pairs = sorted(flower_value_pairs, key=lambda x: x[1], reverse=True)


# Print results
print("++++++++++++++++++++++++")
print(img_path)
for flower, value in sorted_flower_value_pairs:
    print(f"{flower}: {value:.2f}")

print("++++++++++++++++++++++++")
print(predictions)
