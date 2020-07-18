import tensorflow as tf
from tensorflow import keras
#loaded_model = keras.models.load_model('./model.h5')

model = keras.applications.mobilenet.MobileNet()
model.save('./model.h5')