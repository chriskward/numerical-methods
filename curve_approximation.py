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


def interpolate(xarray,yarray):
	
	def funct(x):
		
		if x<xarray.min() or x>xarray.max() : return 0
		if (xarray == x).any(): return yarray[ (xarray == x) ][0]
	 
		max_arg = (xarray > x).argmax()
		min_arg = max_arg-1
		
		return yarray[min_arg] + ((x-xarray[min_arg])/(xarray[max_arg]-xarray[min_arg])) * (yarray[max_arg]-yarray[min_arg])
		
	return funct



def auc(xarray,yarray,a=None,b=None):

	if a == None : a = xarray.min()
	if b == None : b = xarray.min()

	lower_cut = (xarray<=a).argmin()-1
	upper_cut = (xarray<=b).argmin()+1

	xarray = xarray[lower_cut:upper_cut]
	yarray = yarray[lower_cut:upper_cut]

	#percentage deviance from lower_cut and a - scale the first element of area
	#likewise for upper_cut ...


    dx = np.append( np.diff(xarray),[0] )
    dy = np.append( np.diff(yarray),[0] )
    area = (dx*yarray) + (dx*dy*0.5)
    
    return np.sum(area)