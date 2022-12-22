# Dec 2022
# Curve rectification and interpolation 
# using numpy's vectorised operations

import numpy as np

def rectify(func, a = 0, b = 2, epsilon = 0.05, res = 0.001): 
    
    x = np.linspace(a,b, int((b-a)/res) )
    y = func(x)
    
    abs_second_derv = abs( np.gradient( np.gradient(y,x) , x) )
    auc_second_derv = abs_second_derv * res
    cumulative_auc = np.cumsum(auc_second_derv)
    
    x_out , y_out = list([ x[0] ]) , list([ y[0] ])
  
    while cumulative_auc.max() > 0 :
        i = (cumulative_auc > epsilon).argmax()
        if i != 0:
            x_out.append( x[i] )
            y_out.append( y[i] )
        cumulative_auc -= epsilon

    x_out.append(x[-1])
    y_out.append(y[-1])
    
    return np.array(x_out), np.array(y_out)