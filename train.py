import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
import pickle

X = np.array([3,5,6,7,2,4,7,8,9,10,23,45,2,6])
y = np.array([2,6,4,8,76,56,34,12,2,3,6,45,23, 10])

df = pd.DataFrame({"bias" : 1, "X" : X})

lr = LinearRegression()

lr.fit(df, y)

print( lr.predict( pd.DataFrame({"bias":[1], "X": [5]}) ) )
print( lr.predict( np.array([1,5]).reshape(1,-1) ) )

pickle.dump(lr, open("LinearModel.pkl", "wb"))