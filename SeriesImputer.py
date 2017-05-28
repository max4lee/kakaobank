from sklearn.base import TransformerMixin
import numpy as np

class SeriesImputer(TransformerMixin):
    
    def __init__(self):
        """Impute missing values.

        If the Series is of dtype Object, then impute with the most frequent object.
        If the Series is not of dtype Object, then impute with the mean.  

        """
    def fit(self, X, y=None):
        if   X.dtype == np.dtype('O'): self.fill = X.value_counts().index[0]
        else                         : self.fill = X.mean()
        return self

    def transform(self, X, y=None):
       return X.fillna(self.fill)