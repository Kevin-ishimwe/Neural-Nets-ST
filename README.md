# Stock Prediction Neural Networks

This repository contains neural network models for stock prediction. It aims to predict stock price movements using machine learning and deep learning techniques.

![Stock Prediction](https://th.bing.com/th/id/R.7e5e66e788b5dc4469df0296b812e3fb?rik=t8CEujrwf6fPqQ&pid=ImgRaw&r=0)

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Project Description](#project-description)
4. [Data](#data)
5. [Features](#features)
6. [Model Architecture](#model-architecture)
7. [Data Preprocessing](#data-preprocessing)
8. [Training](#training)
9. [Evaluation](#evaluation)
10. [Results](#results)
11. [Dependencies](#dependencies)
12. [Usage](#usage)
13. [Model Architectures](#model-architectures)
14. [Data Preprocessing](#data-preprocessing)
15. [Training](#training)
16. [Evaluation](#evaluation)
10. [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Required libraries and packages (see `requirements.txt` for details)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Kevin-ishimwe/Neural-Nets-ST.git

2. install the  dependencies
```
pip install -r requirements.txt

```
## Project Description

In this project, we aim to predict stock price movements using a neural network. The neural network is designed for binary classification, determining whether the stock price is expected to go up or down based on historical data.
## Data

The project uses historical stock price data for a specific stock (e.g., IBM). The dataset includes various attributes, including open price, close price, high price, low price, volume, and timestamp.
### schema
```
timestamp,open,high,low,close,volume
2023-10-13,139.7700,140.1200,138.2700,138.4600,4583553
2023-10-12,142.5100,142.9300,140.9500,141.2400,3921142
```
## Features

- Close Price: The closing price of the stock.
- Open Price: The opening price of the stock.
- High Price: The highest price of the stock during the trading day.
- Low Price: The lowest price of the stock during the trading day.
- Volume: The trading volume of the stock.
- Timestamp: The date and time of each data point.

## Model Architecture

The neural network architecture used in this project is as follows:

1. Input Layer: Accepts the input features.
2. Hidden Layers: Comprise densely connected layers with ReLU activation functions.
3. Output Layer: Contains a single neuron with sigmoid activation for binary classification.


![feed forward neural networks](https://www.researchgate.net/profile/Junaid-Qadir/publication/348703101/figure/download/fig6/AS:983057658032131@1611390618868/The-overall-architecture-of-the-feedforward-neural-network.ppm)

## Data Preprocessing

Data preprocessing includes the following steps:

- Feature scaling using Min-Max scaling.
- Creating binary labels for price movements.
- Splitting data into training and validation sets.

## Training

The model is trained using the training data with a specified number of epochs. We use the Adam optimizer and binary cross-entropy loss function. Early stopping is also applied to prevent overfitting.

## Evaluation

The model is evaluated using accuracy as the primary metric. Additional metrics such as precision, recall, and F1-score can be considered for evaluation.

## Dependencies

- Python 3.x
- TensorFlow
- Pandas
- Scikit-Learn

## Usage

To train and evaluate the model, you can run the provided code. Be sure to modify the paths and parameters as needed for your specific dataset and use case.

```python
python train_model.py
```
expected logs
```
s: 0.5189 - val_accuracy: 0.7481
Epoch 47/50
76/76 [==============================] - 0s 3ms/step - loss: 0.4642 - accuracy: 0.7830 - val_loss: 0.4094 - val_accuracy: 0.8322
Epoch 48/50
76/76 [==============================] - 0s 3ms/step - loss: 0.4057 - accuracy: 0.8274 - val_loss: 0.4025 - val_accuracy: 0.8314
Epoch 49/50
76/76 [==============================] - 0s 3ms/step - loss: 0.4350 - accuracy: 0.7975 - val_loss: 0.3995 - val_accuracy: 0.8217
Epoch 50/50
76/76 [==============================] - 0s 3ms/step - loss: 0.4170 - accuracy: 0.8137 - val_loss: 0.4276 - val_accuracy: 0.8087
189/189 [==============================] - 0s 945us/step
```
## testing the model 

load the trained model which is the .h5 file and give it the current state for it to predict the next state , keep in mind that moveent label is the close 
```
python main.py
```
output log
```
1/1 [==============================] - 0s 66ms/step
Predicted movement for the next day: 1
```
