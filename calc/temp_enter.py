# -*- coding: utf-8 -*- 

from os import _exit

def t_enter(compounds_in_data):
	while True:
		"""Enter and check temperature if temperature must be lower then minimal of temperature for Cp of this compounds"""
		t = input('Enter temperature in Celsius. Enter "q" and then press ENTER for exit: ')
		try:
			T = int(t) + 273
			if T < 298:
				print ('This temperature is lower then standart - 298 K')
				continue
			elif T > (min([max(x) if type(x) == tuple else x for x in [a[3]['T(Cp)'] for a in compounds_in_data]])):
				# 
				print ("Temperature is higher then the minimum T for Cp %.2f C (%.02f K)" % (((min([max(x) if type(x) == tuple else x for x in [a[3]['T(Cp)'] for a in compounds_in_data]]))-273.15), min([max(x) if type(x) == tuple else x for x in [a[3]['T(Cp)'] for a in compounds_in_data]])))
			else:
				break
		except:
			if t.lower() == 'q':
				_exit(0)
			print ('This is not a number, try again')
	return T