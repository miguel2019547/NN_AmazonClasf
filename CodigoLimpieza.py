import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras

def CargayAnalisisdeDatos():
    dt = pd.read_csv("Datos\_Amazon_products.csv")
    dt.columns = ['','titulo','','','estrellas','comentarios','precio','precio de lista','Categoria', 'mejor vendido','ventas ultimo mes']
    dt.drop('', axis = 1, inplace = True)
    dt['mejor vendido'] = np.where(dt['mejor vendido']==True,1,0)
    dt['precio de lista'] = np.where(dt['precio de lista'] == 0, dt['precio'], dt['precio de lista'])
    dt['oferta'] = np.where(dt['precio de lista']==dt['precio'],1,0)
    return dt

