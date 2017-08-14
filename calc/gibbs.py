# -*- coding: utf-8 -*-
import math

def CpT(dict_, T_react): 			# T_column - name of the column in of Cp temperature in Data
	"""Make a sum of integrals CpT for calculate dST and dHT"""
	T = T_react
	if not dict_['T(Cp)']:
		return 0, 0
	else:
		CpT_S_ = dict_['a']*(math.log(T/298)) + dict_['b']*math.pow(10,-3)*(T-298) - 0.5*dict_['c']*math.pow(10,6)*(math.pow(T, -2) - math.pow(298,-2)) + dict_['d']*(0.5*math.pow(10,-6)*(math.pow(T,2) - math.pow(298,2)))
				
		CpT_H_ = (dict_['a']*(T - 298) + dict_['b']*0.5*math.pow(10,-3)*(math.pow(T,2) - math.pow(298,2)) + dict_['c']*(math.pow(10,6)*(math.pow(298,-1) - math.pow(T, -1))) + dict_['d']*(1/3)*(math.pow(10,-6)*(math.pow(T,3) - math.pow(298,3))))
		return CpT_S_, CpT_H_
		'''
	elif isinstance(dict_['T(Cp)'], tuple):				# This part doesn`t check! 
		"""If more then one values of T(Cp) and 'a', 'b', 'c', 'd' this part calculate a sum of integrals of CpT"""
		T_start = 298										# First temperature of integral calculation
		dCpT_S = []
		dCpT_H = []
		for x in range(len(dict_['T(Cp)'])):
			if dict_['T(Cp)'][x] > T_react:
				T = T_react
			else:
				T = dict_['T(Cp)'][x]
			
			CpT_S_ = (dict_['a'][x]*math.log(T/298)) + (dict_['b'][x]*math.pow(10,-3)*(T-298)) - (0.5*dict_['c'][x]*(math.pow(T, -2) - math.pow(298,-2))) + (dict_['d'][x]*(0.5*math.pow(10,-6)*(math.pow(T,2) - math.pow(298,2))))
			
			CpT_H_ = (dict_['a'][x]*(T - 298) + (dict_['b'][x]*(0.5*math.pow(10,-3)*(math.pow(T,2))) - math.pow(298,2)) + (dict_['c'][x]*(math.pow(10,6)*(math.pow(298,-1) - math.pow(T, -1)))) + (dict_['d'][x]*(1/3*math.pow(10,-6)*(math.pow(T,3) - math.pow(298,3)))))
			
			dCpT_S.append(CpT_S_)
			dCpT_H.append(CpT_H_)
			
			T_start = dict_['T(Cp)'][x]
			if T == T_react:
				return 	(sum(dCpT_S), sum(dCpT_H))
		'''

def gibbs_(dict_, T):
	"""'Accepted a dictionary of thermodynamic data and return Gibbs Free Energy of compound'"""
	dST = dict_['S298'] + CpT(dict_, T)[0]
		
	dHT = dict_['dH298'] + CpT(dict_, T)[1]/1000
		
	return (dHT - T*dST/1000)

	
	
def test():
	dict_ = {'a': 20.56, 'b': -12.6, 'c': -1.78, 'd':0.0, 'T(Cp)':1121.0, 'S298': -0.7, 'dH298': 653.5}
	print (CpT(dict_, 1023))
	print (gibbs_(dict_, 1023))
	return ("Haven't do yet...")
	
if __name__=='__main__':
	print (test())