import numpy as np
from keras.preprocessing import image
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.resnet50 import preprocess_input, ResNet50

# Load pre-trained ResNet50 model trained on ImageNet data
model = ResNet50(weights="imagenet")

# Load and preprocess the image
img_path = "./experiments/project7/predict/3.jpg"
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Make predictions
predictions = model.predict(x)

# Decode and print the top 3 predicted classes
decoded_predictions = decode_predictions(predictions, top=3)[0]
for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
    print("{}. {}: {:.2f}%".format(i + 1, label, score * 100))
