def lms(weight, eta, error, feature):
	res = weight + (eta*error)*feature
	return res