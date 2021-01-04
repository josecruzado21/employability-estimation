  
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.preprocessing import StandardScaler


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
        
class Imputer(BaseEstimator, TransformerMixin):

    def __init__(self,columns):
        self.columns=columns
    
    def fit(self, X):
        self.imputer=IterativeImputer(max_iter=15,random_state=0)
        self.imputer.fit(X)
        return self
    
    def transform(self, X):
        data=X.copy()
        X_imputar=pd.DataFrame(self.imputer.transform(X),columns=X.columns)
        for i in list(self.columns):
            data[i]=X_imputar[i]
        return data
    
class Encoder(BaseEstimator, TransformerMixin):
    def __init__(self,columns):
        self.columns=columns

    def fit(self, X):
        return self
    
    def transform(self, X):
        data=X.copy()
        return pd.get_dummies(data,columns=self.columns)
    
class Scaler(BaseEstimator,TransformerMixin):
    def __init__(self,columns):
        self.columns=columns
    
    def fit(self,X):
        self.scaler=StandardScaler()
        self.scaler.fit(X)
        return self
    def transform(self,X):
        data=X.copy()
        X_scaled=pd.DataFrame(self.scaler.transform(X),columns=X.columns)
        for i in list(self.columns):
            data[i]=X_scaled[i]
        return data