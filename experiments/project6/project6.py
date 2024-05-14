import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pathlib

# Downloads a file from a URL if it not already in the cache.
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file(
    "flower_photos.tar", origin=dataset_url, extract=True
)
data_dir = pathlib.Path(data_dir).with_suffix("")

image_count = len(list(data_dir.glob("*/*.jpg")))
print(image_count)

# Size images we are going to input in the neural network
batch_size = 32
img_height = 180
img_width = 180

# Image augmentation
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest",
)

# Generates a tf.data.Dataset from image files in a directory for training
train_ds = train_datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode="binary",
)

# Generates a tf.data.Dataset from image files in a directory for validation
val_datagen = ImageDataGenerator(rescale=1.0 / 255)

val_ds = val_datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode="binary",
)

# Print the labels
class_names = train_ds.class_indices
print(class_names)

# Create the model with Sequential (groups a linear stack of layers)
num_classes = len(class_names)
model = Sequential(
    [
        layers.Conv2D(
            16,
            3,
            padding="same",
            activation="relu",
            input_shape=(img_height, img_width, 3),
        ),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dense(num_classes),
    ]
)

# Compile the model and print summary
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"],
)
model.summary()

# Train the model
epochs = 10
history = model.fit(train_ds, validation_data=val_ds, epochs=epochs)

# Save model to file for reuse
model.save("./experiments/project6/model.keras")

# Print a chart to analyze the model
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend(loc="lower right")
plt.title("Training and Validation Accuracy")

plt.subplot(1, 2, 2)
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend(loc="upper right")
plt.title("Training and Validation Loss")
plt.show()
