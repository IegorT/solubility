# -*- coding: utf-8 -*-
import os
from math import exp
from sympy import var, expand, solve
from numpy import roots,real

from calc import task_parse, data_loc, gibbs, temp_enter
R = 8.314

location = '%s' % os.path.dirname(os.path.abspath(__file__)) + '/data/therm_data.xls'     	# location xls data file
data = data_loc.location(location)															# open end parse data file by pandas

compounds_in_data = task_parse.compounds_list(data)											# list [index, compounds, coeff, {dict of Thermodynamic function}]
T =  temp_enter.t_enter(compounds_in_data)

dG = sum([gibbs.gibbs_(a[3], T)*a[2] for a in compounds_in_data])							# Gibbs Free Energy
K = exp(-1*dG*1000/(R*T))																	# Constants of the reaction


mol = float(input('Enter mol % of solvent :'))
x = var('x', real = True)
c = compounds_in_data[2][2]
d = compounds_in_data[3][2]
b = compounds_in_data[1][2]
b_ = b
if K < 10**(-30):
	b_ = 0
C = (c*x)**c              
D = (d*x)**d             
B = (mol+ b_*x)**abs(b)              
rate = (c+b+d)

if rate > 1:
	sol = expand(C*D*(1+rate*x)**rate - B*K)
else:
	sol = expand(C*D- B*K*(1+rate*x)**abs(rate))
	
#answer = solve(sol)
answer_ =  [x.real for x in roots([sol.coeff(x, n) for n in range(6)][::-1]) if x > 0 and x < 0.5]

print (answer_)
