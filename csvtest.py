import pandas as pd
import os.path
import time


def test():
	df = pd.read_csv("StudySessions.csv",index_col='ID')
	for index, row in df.iterrows():
		Date = row['Date']
		Session = row['Session']
		Start = row['Start']
		End = row['End']
		print(f'Index is {index}')
		print(f'Date is is {Date} and Session Length is {Session}')
	print(index)
	df = df.append({'ID':f'{index+1}','Date': 'today', 'Start':1, 'End':2 }, ignore_index=True)
	df.to_csv("StudySessions.csv")


def write():
	df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
	                   'mask': ['red', 'purple'],
	                   'weapon': ['sai', 'bo staff']})
	df.to_csv('/Users/sahilbambulkar/GithubFiles/FocusedSquared/test.csv')


test()