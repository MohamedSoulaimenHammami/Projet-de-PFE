# Importing the libraries
import numpy as np
from utils import *

bat = float(input('donner la valeur de bat \n'))
if bat <20 : 
    print("we cant support this ")
else :

    C= float(input('donner C\n'))
    V = float(input('donner V\n'))
    T = float(input('donner T\n'))
    P = float(input('donner P\n'))
    BW = float(input('donner BW\n'))
    

    to_predict= format(C,V, T, P, BW)
    file_name = '/home/msh/Desktop/freelance/houssem/classifier.sav' # badel l emplacement 
    classifier = load_model(file_name)

    prediction = make_prediction(classifier , to_predict)
    print(prediction)