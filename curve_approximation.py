# Dec 2022
# Curve rectification and interpolation 
# using numpy vectorised operations

# A collection of tools to represent a smooth function
# with an optimally places set of points (x1,y1), (x2,y2), ...

# These functions are used extensively in my random-variable repo
# to represent and work with probability density functions as collections of points

import numpy as np

def rectify(func, a = 0, b = 2, epsilon = 0.05, res = 0.001): 
    
    # initially we approximate the function with a large set of sampled points
    
    x = np.linspace(a,b, int((b-a)/res) )
    y = func(x)

    # We compute the modulus second derivative
    
    abs_second_derv = abs( np.gradient( np.gradient(y,x) , x) )

    # Then the area under the second derivative

    auc_second_derv = abs_second_derv * res
    
    # Then the cumulative (absolute) area under the second derivative

    cumulative_auc = np.cumsum(auc_second_derv)
    
    x_out , y_out = list([ x[0] ]) , list([ y[0] ])

    # and select points such that the integral between any two points
    # of the absolute value of the 2nd derivative is less that epsilon
    # (sections of curve with rapidly changing curvature will be approx
    # imated by more points than sectons that are closer to linear) 
  
    while cumulative_auc.max() > 0 :
        i = (cumulative_auc > epsilon).argmax()
        if i != 0:
            x_out.append( x[i] )
            y_out.append( y[i] )
        cumulative_auc -= epsilon

    x_out.append(x[-1])
    y_out.append(y[-1])
    
    return np.array(x_out), np.array(y_out)


def interpolate(xarray,yarray):
    
    # returns a function that will return y=f(x) for
    # any value of x in the domain of f.

    # f() is approximated by two arrays of points, xarray and yarray
    # The returned function will interpolate values of y that lie between
    # points.

    def funct(x):
               
        def _compute_y(x):

            # if x corresponds to a value outside the domain
            # return 0

            if x<xarray.min() or x>xarray.max() : return 0
            
            # if x corresponds to an actual point in xarray, return the 
            # corresponding value of yarray

            if (xarray == x).any(): return yarray[ (xarray == x) ][0]
     
            # if x corresponds to a point between values in xarray
            # find the immediate points <x and >x and interpolate 
            # with a straight line  

            max_arg = (xarray > x).argmax()
            min_arg = max_arg-1
        
            return yarray[min_arg] + ((x-xarray[min_arg])/(xarray[max_arg]-xarray[min_arg])) * (yarray[max_arg]-yarray[min_arg])
        
        # the function we return is not, as a result of the code above, vectorised
        # if it is passed a numpy array, iterate through the array (to give the API the illusion of vectorised operation)

        if isinstance(x,np.ndarray):
            return np.array( [_compute_y(i) for i in x] )
        else:
            return _compute_y(x)
        
    return funct



def auc(xarray,yarray,a=None,b=None):

    if a == None or a<xarray.min() : a = xarray.min()
    if b == None or b>xarray.max() : b = xarray.max()

    lower_cut = (xarray<=a).argmin()-1
    upper_cut = (xarray<b).argmin()+1
    
    xarray = xarray[lower_cut:upper_cut]
    yarray = yarray[lower_cut:upper_cut]

    #percentage deviance from lower_cut and a - scale the first element of area
    #likewise for upper_cut ...

    lower_y_scale = xarray[1]-a / xarray[1]-xarray[0]
    upper_y_scale = b-xarray[-2] / xarray[-1]-xarray[-2]

    xarray[0]  = a
    xarray[-1] = b

    # first and final values in y array - the y-vals that 
    # correspond to a,b

    yarray[0] =  yarray[1]  - ( (yarray[1]-yarray[0])   *lower_y_scale)
    yarray[-1] = yarray[-1] - ( (yarray[-1]-yarray[-2]) *upper_y_scale)

    dx = np.append( np.diff(xarray),[0] )
    dy = np.append( np.diff(yarray),[0] )

    area = (dx*yarray) + (dx*dy*0.5)
    
    return np.sum(area)