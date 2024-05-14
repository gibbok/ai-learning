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

img = tf.keras.utils.load_img(
    "./experiments/project6/flower_photos/daisy/15207766_fc2f1d692c_n.jpg",
    target_size=(img_height, img_width),
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create a batch

model = keras.models.load_model("./experiments/project6/model.keras")

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

# ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
print(predictions)

# ./experiments/project6/flower_photos/dandelion/8475769_3dea463364_m.jpg
# [[-1.8662428  2.7576375 -1.3162225  6.6833487 -4.452546 ]]

# ./experiments/project6/flower_photos/daisy/15207766_fc2f1d692c_n.jpg
# [[ 5.5258045  3.550712  -1.2611673 -2.4062922  0.5262111]]
