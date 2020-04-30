import numpy as np

def simulate(bias, coefficient, type, paras):

	# Normal Distribution
	if type.strip() == 'normal':
		variate=np.random.normal(loc=paras[0], scale=paras[1])
		result = bias + coefficient * variate

	# Uniform Distribution
	elif type.strip() == 'uniform':
		variate=np.random.uniform(low=paras[0], high=paras[1])
		result = bias + coefficient * variate


	# Poisson Distribution
	elif type.strip() == 'poisson':
		variate=np.random.poisson(lam=paras[0])
		result = bias + coefficient * variate

	# Binomial Distribution
	elif type.strip() == 'binomial':
		variate=np.random.binomial(n=paras[0],p=paras[1])
		result = bias + coefficient * variate

	# Beta Distribution
	elif type.strip() == 'beta':
		variate=np.random.uniform(a=paras[0], b=paras[1])
		result = bias + coefficient * variate

	# gamma Distribution
	elif type.strip() == 'gamma':
		variate=np.random.uniform(shape=paras[0], scale=paras[1])
		result = bias + coefficient * variate

	# Weibull Distribution
	elif type.strip() == 'weibull':
		variate=np.random.uniform(a=paras[0])
		result = bias + coefficient * variate

	elif type.strip() == 'None':
		result = bias

	else:
		raise Exception('Distribution is not included or spelled incorrectly.')

	return result
