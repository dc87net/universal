#! /usr/bin/env python3

#
from sympy import symbols, integrate, sqrt, cos

# Define the symbolic variables
G, M, c, a, r, theta = symbols('G M c a r theta')
rho_m = symbols('rho_m', constant=True)


# Gravitational potential energy integral
U_equator = - integrate(G * rho_m * M / sqrt(r**2 + a**2 * cos(theta)**2), (theta, 0, 2 * 3.14159))
print(U_equator)


# Work done by spacetime pressure integral
W_equator = integrate(G * rho_m * sqrt(r**2 + a**2 * cos(theta)**2), (theta, 0, 2 * 3.14159))
print(W_equator)
#
# from sympy import symbols, integrate, sqrt, cos, pi
#
# # Define the symbolic variables
# G, M, c, a, r, theta = symbols('G M c a r theta')
# rho_m = symbols('rho_m', constant=True)
#
# # Gravitational potential energy integral
# U_equator = - 2 * integrate(G * rho_m * M / sqrt(r**2 + a**2 * cos(theta)**2), (theta, 0, pi))
# print(U_equator)
#
# # Work done by spacetime pressure integral
# W_equator = 2 * integrate(G * rho_m * sqrt(r**2 + a**2 * cos(theta)**2), (theta, 0, pi))
# print(W_equator)
