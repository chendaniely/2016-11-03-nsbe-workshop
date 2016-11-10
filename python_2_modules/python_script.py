def c2f(temp):
	convert = (9/5) * temp + 32
	return(convert)

def k2c(temp):
	return(temp - 273.15)

def k2f(temp):
	c = k2c(temp)
	f = c2f(c)
	return(f)
