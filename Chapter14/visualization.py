import matplotlib.pyplot as plt 
import numpy as np 

data = [25., 5., 150., 100.] 
x_values = range(len(data)) 
plt.bar(x_values, data) 

plt.show() 

plt.bar(x_values, data, width=1.)  

plt.show() 
    

        
        
data = [ [8., 57., 22., 10.], 
            [16., 7., 32., 40.],
           ] 

 
import matplotlib.pyplot as plt2 
x_values1 = np.arange(4) 
plt2.bar(x_values1 + 0.00, data[0], color='r', width=0.30) 
plt2.bar(x_values1 + 0.30, data[1], color='y', width=0.30) 

plt2.show() 
    
    
import numpy as np 
import matplotlib.pyplot as plt 

data = np.random.randn(50) 

plt.boxplot(data) 
plt.show() 
    
    
import matplotlib.pyplot as plt 
data = [500, 200, 250] 

labels = ["Agriculture", "Aide", "News"] 

plt.pie(data, labels=labels,autopct='%1.1f%%') 
plt.show() 
    
    
    
import numpy as np 
import matplotlib.pyplot as plt 


n = 10 
x = np.random.rand(n) 
y = np.random.rand(n) 
colors = np.random.rand(n) 
area = np.pi * (60 * np.random.rand(n))**2 

plt.scatter(x, y, s=area, c=colors, alpha=0.5) 
plt.show() 