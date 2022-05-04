
import pickle
import numpy as np 


def load_model(file_name):
  loaded_model = pickle.load(open(file_name, 'rb'))
  return loaded_model

def make_prediction(model , to_predict):
  result=model.predict(to_predict)
  return result

def format(C,V, T, P, BW) : 
    return np.array([[C,V, T, P, BW]])