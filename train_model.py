import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
#the test is gonna be running the IBM stock data through the neural network
data =pd.read_csv("./datasets/IBM/daily_stock_data.csv")

data['daily_return'] = data['close'].pct_change()
data['timestamp']=pd.to_datetime(data['timestamp'])
data['year']=data['timestamp'].dt.year
data['month']=data['timestamp'].dt.month
data['day'] = data['timestamp'].dt.day


scaler=MinMaxScaler()
data[['open','close','high','low','volume']]=scaler.fit_transform(data[['open','close','high','low','volume']])

# neural network architecture for binary classification
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(5,)),          # input layer with 7 features
    tf.keras.layers.Dense(128, activation='linear'),  # hidden layer with 64 neurons and ReLU activation
    tf.keras.layers.Dense(128, activation='linear'),  # another hidden layer
    tf.keras.layers.Dense(1, activation='sigmoid')  # output layer with sigmoid activation for binary classification
])


model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
data['movement_label'] = (data['close'].shift(-1) > data['close']).astype(int)

model.summary()
X = data[['open','close','high','low','volume']]
y = data['movement_label']
model.fit(X, y, epochs=50, validation_split=0.6)  
predicted_probabilities = model.predict(X)
predicted_binary = (predicted_probabilities>0.5).astype(int)
accuracy = accuracy_score(y, predicted_binary)
model.save("./models/IBM_model_iteration_1.0.h5")
print(f"Accuracy: {accuracy}")


