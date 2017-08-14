# -*- coding: utf-8 -*-
import pandas as pd

def location(location=''):
	while True:
		"""Connecting the Thermodynamic data file"""
		if not location:
			location = input('Input the path of data file (*.xls) location, or "q" and then press ENTER for exit:  ')
			try:
				if msvcrt.getch() == b'q':
					os._exit(0)
			except:
				print('There is no such file or directory')
				continue
		break
	return pd.read_excel(location, sheetname = 'Term', encoding='utf-8')

def test():
	return ("Haven't do it yet!")
	
	
if __name__=='__main__':
	print (test())