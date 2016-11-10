import python_script as ps

assert(ps.c2f(0) == 32)
assert(ps.c2f(100) == 212)

assert(ps.k2c(273.15) == 0)
assert(ps.k2c(0) == -273.15)

assert(ps.k2f(273.15) == 32)
