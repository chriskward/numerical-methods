import numpy as np

def mae(y,y_hat):

	signed_loss = (y_hat-y)
	f = lambda x: 1 if x>0 else -1
	grad = np.apply_along_axis(f,1,signed_loss)
	grad = np.expand_dims(grad, axis = 1)
	loss = np.sum( np.abs(signed_loss) )

	return loss,grad


def mse(y,y_hat):

	loss = np.sum( (y - y_hat)**2 )
	grad = -2*(y-y_hat)

	return loss,grad


def optimiser(x,y,lr=0.01,loss='mae',epochs=5):

	if loss=='mae' : loss_function = mae
	elif loss=='mse' : loss_function = mse
	else: raise AttributeError(" loss must be 'mse' or 'mae' only ")

	consts = np.ones(( x.shape[0],1 ))
	x = np.hstack(( consts,x ))

	beta = np.random.randn( x.shape[1],1 )

	loss_list = list()

	for i in range(epochs):

		y_hat = x @ beta

		loss,dl_dy = loss_function(y,y_hat)
		loss_list.append(loss)

		dy_db = x
		dl_db = dl_dy * dy_db

		param_update = np.sum(dl_db,axis=0,keepdims=True).T * lr

		beta -= param_update

	return loss_list, beta
