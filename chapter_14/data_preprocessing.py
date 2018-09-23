
import numpy as np 
import pandas 
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Binarizer

data = pandas.DataFrame([ 
        [4., 45., 984.], 
        [np.NAN, np.NAN, 5.], 
        [94., 23., 55.], 
    ]) 

print(data)

print(data.fillna(0.1)) 

print(data.fillna(data.mean())) 

data1 = pandas.DataFrame([[  58.,   1.,   43.],
 [  10.,  200.,   65.],
 [  20. ,  75. ,   7.]])

scaled_values = MinMaxScaler(feature_range=(0,1)) 
results = scaled_values.fit(data1).transform(data1) 
print(results) 

stand_scalar =  StandardScaler().fit(data1) 
results = stand_scalar.transform(data1) 
print(results)

results = Binarizer(50.0).fit(data1).transform(data1) 
print(results) 
    
    
    
    
    
