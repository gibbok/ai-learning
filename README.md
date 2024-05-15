# AI Learning

This repository hosts multiple `python` projects focused on AI learning.

All code examples are well-commented, making them suitable for use as self-tutorials.

## Project 1

Prediction using linear regression using `sklearn` and visualization using `matplotlib` and `seaborn`.

[Visit](./experiments/project1/README.md)

## Project 2

Expenditure prediction using linear regression with `sklearn` and `matplotlib`.

[Visit](./experiments/project2/README.md)

## Project 3

Sentiment analysis using `sklearn` and `pandas`, visualization using `matplotlib`.

[Visit](./experiments/project3/README.md)

## Project 4

Data analysis with network diagrams using `networkx`, `pandas`, and `matplotlib`.

[Visit](./experiments/project4/README.md)

## Project 5

Analyze frequency and decision tree classification using `sklearn`, `matplotlib`, `pandas`, and `seaborn`.

[Visit](./experiments/project5/README.md)

## Project 6

Image classification with neural network using `tensorflow`, `matplotlib`, and `numpy`.

[Visit](./experiments/project6/README.md)

## Project 7

Image classification using pre-trained ResNet50 model trained on ImageNet data using `keras`.

[Visit](./experiments/project7/README.md)

### Developer Tools

To run the project:

```shell
cd experiments
poetry shell
cd ../
make p1
```

Use the `make` command to run each project. For instance, project 2 is `make p2`, and project 3 is `make p3`.

Or using Jupyter Notebook:

```shell
cd experiments/project1
jupyter notebook
```

Or open Visual Studio Code with the root folder, and press `F5` to start debugging.

To add a dependency with Poetry:

```shell
cd experiments
poetry add YOUR_DEPENDENCY
```
