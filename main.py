import pandas as pd
import tensorflow as tf


loaded_model = tf.keras.models.load_model("./models/IBM_model_iteration_1.1.h5")

current_state = pd.DataFrame({
    'close': [129.64]
})


predictions = loaded_model.predict(current_state)
predicted_label = (predictions).astype(int)
print("Predicted movement for the next day:",predicted_label)

