import numpy as np
from tensorflow.keras.applications import MobileNet, imagenet_utils
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model
from tensorflow.keras.applications import imagenet_utils

# Define the input shape for the image
img_shape = (224, 224, 3)

# Load the pre-trained MobileNet model
mobilenet = MobileNet(weights="imagenet", include_top=False, input_shape=img_shape)

# Freeze the pre-trained model layers (not train them)
for layer in mobilenet.layers:
    layer.trainable = False

# Add a new classifier layer for our specific number of classes
x = mobilenet.output
predictions = Dense(10, activation="softmax")(x)  # Change 10 to your num_classes

# Create the final model
model = Model(inputs=mobilenet.input, outputs=predictions)

# Compile the model (define optimizer and loss function)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Load and pre-process your image
img = image.load_img("./experiments/project7/predict/1.jpg", target_size=img_shape)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)  # Add a batch dimension
x = imagenet_utils.preprocess_input(x)  # Apply pre-processing for MobileNet

# Make prediction on the image
predictions = model.predict(x)

# Decode the predicted class
predicted_class_idx = np.argmax(predictions[0])

# Load ImageNet labels
with open("./experiments/project7/imagenet_labels.txt", "r") as f:
    labels = f.readlines()

# Print the human-readable prediction (remove extra space before label)
print(f"Predicted class: {labels[predicted_class_idx].strip()}")
