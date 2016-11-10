# if you run the command nosetests
# in the terminal
# it will look for this file and run the
# tests in this file

import python_script as ps

def test_c2f():
	assert(ps.c2f(0) == 32)
	assert(ps.c2f(100) == 212)

def test_k2c():
	assert(ps.k2c(273.15) == 0)
	assert(ps.k2c(0) == -273.15)

def test_k2f():
	assert(ps.k2f(273.15) == 32)
