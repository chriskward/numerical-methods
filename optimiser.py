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
	"""
	optimiser(x,y, lr=0.01, loss='mae', epochs=5) -> loss_list: list  ,  beta: ndarray

	x: nd.array.shape(n,p)  (n: no data samples, p: no covariates)
	y: no.array.shape(n,1)	(column vector of target values)

	lr: float
	learning rate

	loss: str
	'mae' mean absolute error
	'mse' mean squared error

	epochs: int
	"""

	# select chosen loss function

	if loss=='mae' : loss_function = mae
	elif loss=='mse' : loss_function = mse
	else: raise AttributeError(" loss must be 'mse' or 'mae' only ")

	# append a column of 1's to data matrix
	# the coefficient for the constant term

	consts = np.ones(( x.shape[0],1 ))
	x = np.hstack(( consts,x ))

	# random initialisation of parameters

	beta = np.random.randn( x.shape[1],1 )

	loss_list = list()

	for i in range(epochs):

		y_hat = x @ beta

		loss,dl_dy = loss_function(y,y_hat)
		loss_list.append(loss)

		# the variables below are technically the 
		# vector jacobian products rather than the 
		# jacobians. Their names are perhaps misleading

		dy_db = x
		dl_db = dl_dy * dy_db

		# update the parameters

		param_update = np.sum(dl_db,axis=0,keepdims=True).T * lr
		beta -= param_update

	return loss_list, beta
