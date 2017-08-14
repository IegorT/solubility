# -*- coding: utf-8 -*- 
from os import _exit
from ast import literal_eval															# form str to tuple

def task_parse(lst_data, task):
	"""This function accept compounds list from data file and equation and return a list (compound, number in list data, coefficient, if it in the right side is negative)"""
	task = task.replace(' ','').replace('+', ' ').replace('=', ' ').split() 
	# aA + bB = cC + dD --> ['aA', 'bB', 'cC', 'dD']
	compounds = []
	for compound in task:				
		if compound[0].isdigit():
			coeff = int(compound[0])
			comp = compound[1:]
		elif compound[0].isupper() and compound[0].isalpha():
			coeff = 1
			comp = compound
		else: 
			return "This is not a compound"
		if task.index(compound) < 2 and len(task) > 2:
			coeff = -coeff
		checked_comp = compound_in_data(lst_data, comp)
		if type(checked_comp) != tuple:													# if no compound in data list return 'The compound is not in data file'
			return checked_comp
		compounds.append([checked_comp[0], checked_comp[1], coeff])
		# [[lst_data.index('A'), 'A', -a], [lst_data.index('B'), 'B', -b], [lst_data.index('C'), 'C', c], [lst_data.index('D'), 'D', -d]]
	return compounds
	
def compound_in_data(lst_data, compound):
	"""This part is checking if the compound present in data(lst_data) or not"""
	try:
		lst_data.index(compound)
		return lst_data.index(compound),compound
	except:
		return ('The %s is not in data file' % compound)

def enter_equation(lst_compounds):
	"""Enter the equation of the reaction"""
	while True:
		equation = input('Enter equation, for exemple: ZrO2 + 4LiF = 2Li2O + ZrF4, or compound. Enter "q" and then press ENTER for exit:\n')
		if not equation:
			equation = 'ZrO2 + 4LiF = 2Li2O + ZrF4'
		elif equation.lower() == 'q':
			_exit(0)
		compounds_in_data = task_parse(lst_compounds, equation)
		if type(compounds_in_data[0]) == list:
			return compounds_in_data
		else:
			print (compounds_in_data)

def compounds_list(data, equation=None):
	"""Return a list of compounds with a dict of its Thermodynamic functions"""
	td_func = ['dH298', 'S298', 'a', 'b', 'c', 'd', 'T(Cp)']							# list of Thermodynamics functions for dictionary
	lst_compounds = [x for x in data['Compound']]										# list of compounds in data
	if not equation:																	# if not equation or compound enter it
		compounds_in_data = enter_equation(lst_compounds)
	else:																			    # Has not checked! For automatic calculation
		compounds_in_data = task_parse(lst_compounds, equation)
	for compound in compounds_in_data:
		dct = {}																		# a dictionary of Thermodynamic functions for each compound in equation
		for td in td_func:
			if type(data[td][compound[0]]) == str:
				num = literal_eval(data[td][compound[0]])								# if in the data_file is more then 1 value make a tuple of this values
			else:
				num = data[td][compound[0]]
			dct[td] = num
		compounds_in_data[compounds_in_data.index(compound)].append(dct)
	# [[lst_data.index('A'), 'A', -a], [lst_data.index('B'), 'B', -b], [lst_data.index('C'), 'C', c], [lst_data.index('D'), 'D', -d]]
	return compounds_in_data
		
	
	
def test():
	lst = ['NaCl', 'NaF', 'NaNO3', 'Na2O', 'KCl', 'KF', 'KNO3', 'K2O', 'EuCl3', 'EuF3', 'Eu2O3']
	tsk1 = 'Eu2O3 + 6NaF = 3Na2O + 2EuF3'
	tsk2 = 'EuF3+Na2O=EuOF+2NaF'
	tsk3 = "lkl,"
	compound1 = 'NaF'
	compound2 = 'Na2O'
	compound3 = 'Eu2O3'
	compound4 = 'EuF3'
	compound5 = 'EuOF'
	assert task_parse(lst, tsk1) == [[lst.index(compound3), compound3, -1], [lst.index(compound1), compound1, -6], [lst.index(compound2), compound2, 3], [lst.index(compound4), compound4, 2]]
	assert task_parse(lst, tsk2) == 'The %s is not in data file' % compound5
	assert task_parse(lst, tsk3) == 'This is not a compound'
	return ('The test functions is pass')
		
	
if __name__=='__main__':
	print (test())