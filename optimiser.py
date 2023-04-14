import numpy as np

def mae(y,y_hat):

	signed_loss = (y-y_hat)
	f = lambda x: 1 if x>0 else -1
	grad = np.apply_along_axis(f,1,signed_loss)
	loss = np.abs(signed_loss)

	return loss,grad


def mse(y,y_hat):

	loss = (y - y_hat)**2
	grad = -2(y-y_hat)

	return loss,grad


def optimiser(x,y,lr=0.01,loss='mae',epochs=5):

	consts = np.ones(( x.shape[0],1 ))
	x = np.hstack(( consts,x ))

	beta = np.random.randn( x.shape[1],1 )


