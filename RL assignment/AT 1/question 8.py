import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(16, activation="relu", input_shape=(4,)),
    keras.layers.Dense(16, activation="relu"),
    keras.layers.Dense(1)
])

model.compile(optimizer="adam",
              loss="mse",
              metrics=["accuracy"])

model.summary()
