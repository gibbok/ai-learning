# image-classification

Flower Classification with TensorFlow.

## Input

Images of various flower species.

[Source data]([XXX](https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz))


## Output

- Classify new flower images using the trained model.

## Results

1. Data Loading and Preprocessing: The code loads the Flower Photos dataset from a URL and preprocesses the images for training and validation.
2. Image Augmentation: Image augmentation techniques such as rotation, shifting, shearing, zooming, and flipping are applied to generate diverse training samples and improve the model's generalization.
3. Model Creation: A convolutional neural network (CNN) is created using the Sequential API of Keras. The CNN consists of convolutional layers followed by max-pooling layers, flattening, and fully connected layers.
4. Model Training: The model is compiled with appropriate loss function and optimizer, then trained on the training dataset for a specified number of epochs.
5. Model Evaluation: The training and validation accuracies and losses are plotted to visualize the training progress and assess the model's performance.
6. Model Saving: Once trained, the model is saved to a file for future use. Use file `use-model.py` to run the pre-trained model.


![result](./assets/result.png)

Samples:

```text
roses: 1765.41
tulips: 1287.42
daisy: 354.11
sunflowers: -278.38
dandelion: -836.83
```