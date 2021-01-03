from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
        
class Undersample(BaseEstimator, TransformerMixin):
    def __init__(self,porcentaje):
        self.porcentaje=porcentaje

    def fit(self, X, y):
        return self
    
    def transform(self, X,y):
        # Primero copiamos el dataframe de datos de entrada 'X'
        aceptados_train=X[y=='Aceptado'].shape[0]
        noaceptados_train=X[y!='Aceptado'].shape[0]
        todo=pd.concat([X,y],axis=1)
        X1=todo.copy()[todo['OBJETIVO']=='Aceptado'].sample(int(round(noaceptados_train+(aceptados_train-noaceptados_train)*self.porcentaje)))
        X2=todo.copy()[todo['OBJETIVO']!='Aceptado']
        Xs=pd.concat([X1,X2])[X.columns]
        ys=pd.concat([X1,X2])['OBJETIVO']
        return (Xs,ys) 