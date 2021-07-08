import csv
from datetime import date


def addtoCSV():
	with open('Example.csv','r') as csv_file:
		csv_reader = csv.reader(csv_file)

		with open('new_names.csv','w') as new_file:
			csv_writer = csv.writer(new_file, delimiter=',')

			for line in csv_reader:
				csv_writer.writerow(line)


def addtoDictCSV():
	with open('Example.csv','r') as csv_file:
		csv_reader = csv.DictReader(csv_file)


		for line in csv_reader:
			print(line)
			#if str(date.today())==line['Date']:
				
		return

		with open('new_names.csv','w') as new_file:
			fieldnames = ['Date','Time Studied (Hours)','Study Session (Minutes)']
			csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

			csv_writer.writeheader()

			for line in csv_reader:
				csv_writer.writerow(line)



addtoDictCSV()