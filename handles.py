import csv
with open('test.csv', newline='\n') as input:
	reader = csv.reader(input, delimiter=' ')
	for row in reader:
		handle = row.pop()
		for site in row:
			if site == 'am':
				print(f'host *= "amazon"i & path *= "{handle}"'
