# Code copied from https://www.tensorflow.org/datasets/keras_example

import mlflow

from params import TrainConfig

import tensorflow_datasets as tfds
import tensorflow as tf

import mlflow.tensorflow

mlflow.tensorflow.autolog()  # Start the MLFlow tracker to log all default tensorflow parameters

# Load the data as specified by the Data Repository
(ds_train, ds_test), ds_info = tfds.load(
    "my_augmented_mnist",
    split=["train", "test"],
    shuffle_files=True,
    as_supervised=True,
    with_info=False,
    data_dir="augmented_mnist/data/tensorflow_datasets"
)


def normalize_img(image, label):
    """Normalizes images: `uint8` -> `float32`."""
    return tf.cast(image, tf.float32) / 255.0, label


# Process the training data
ds_train = ds_train.map(normalize_img, num_parallel_calls=tf.data.experimental.AUTOTUNE)
ds_train = ds_train.cache()
ds_train = ds_train.shuffle(ds_info.splits["train"].num_examples)
ds_train = ds_train.batch(128)
ds_train = ds_train.prefetch(tf.data.experimental.AUTOTUNE)


# Process the test data
ds_test = ds_test.map(normalize_img, num_parallel_calls=tf.data.experimental.AUTOTUNE)
ds_test = ds_test.batch(128)
ds_test = ds_test.cache()
ds_test = ds_test.prefetch(tf.data.experimental.AUTOTUNE)


# Define a simple model.
model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(10),
    ]
)
model.compile(
    optimizer=tf.keras.optimizers.Adam(TrainConfig.LEARNING_RATE),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=[tf.keras.metrics.SparseCategoricalAccuracy()],
)

# Model fitting
model.fit(
    ds_train,
    epochs=TrainConfig.EPOCHS,
    validation_data=ds_test,
)
