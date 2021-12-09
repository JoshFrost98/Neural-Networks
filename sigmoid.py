import numpy as np

def sigmoid(z):
    
    output = 1/(1+np.exp(-z))
    #########################################
    # Write your code here
    # modify this to return z passed through the sigmoid function
    
    ########################################/
    
    return output
