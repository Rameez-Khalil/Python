import numpy as np
from numpy.random import randn


x = round(randn()*10)
if(x>1): 
    print("Greater than 1")
    print(x)
else: 
    print("Not Greater than 1")
    print(x)