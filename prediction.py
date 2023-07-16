import tensorflow as tf
import numpy as np
import pandas as pd
import IPython.display as ipd
import librosa
import matplotlib.pyplot as plt
from keras.models import load_model

def create_predict_dataset(data,a=12000):
  dataset=data[:a]
  dataset=np.reshape(dataset,(1,a,1))
  for i in range(1,int(data.shape[0]/a)):
    dataset=tf.concat([dataset,np.reshape(data[i*a:a*(i+1)],(1,a,1))],axis=0)
  dataset=tf.concat([dataset,np.reshape(data[-a:],(1,a,1))],axis=0)
  diff=len(data)%a
  return dataset,diff

def predict_dataset(dataset,diff,a=12000):
  model=load_model('models/model3.h5')
  predict=model.predict(dataset)
  predict=predict.flatten()
  predict=tf.concat([predict[:-a],predict[-diff:]],axis=0)
  return predict

# data=librosa.load('/content/drive/MyDrive/Colab Notebooks/noise download/noise1.wav')[0]

def predict_output(data):
    dataset,diff=create_predict_dataset(data)
    prediction=predict_dataset(dataset,diff)
    return prediction