import pandas as pd
import tensorflow as tf


loaded_model = tf.keras.models.load_model("./models/IBM_model_iteration_1.0.h5")
#'open','close','high','low','volume'
current_state = pd.DataFrame({
    'close': [129.64],
    'open': [126.12],
    'high': [132.64],
    'low': [122.64],
    'volume': [3223566]
})


predictions = loaded_model.predict(current_state)
predicted_label = (predictions).astype(int)
print("Predicted movement for the next day:",predicted_label[0][0])

