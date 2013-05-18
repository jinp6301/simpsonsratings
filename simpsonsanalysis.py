import csv
from math import sqrt


datafile = open('simpsons4.csv', 'rU')
datareader = csv.reader(datafile)
data = []
for row in datareader:
	data.append(row)

def stdv(x):
	n, mean, std = len(x), 0, 0
	for a in x:
		mean = mean + a
		mean = mean / float(n)
	for a in x:
		std = std + (a - mean)**2
		try:
			std = sqrt(std / float(n-1))
		except:
			std = 0
	return std


writers = []
for i in range(1, len(data)):
	writers.append(data[i][5])

writerslist = list(set(writers))

totalwriter = []
totalwriter.append(['writer','average rating','standard deviation'])
for i in range(len(writerslist)):
	writer1 = []
	for j in range(1, len(data)):
		if writerslist[i] == data[j][5]:
			writer1.append(float(data[j][4]))
	totalwriter.append([writerslist[i], sum(writer1)/float(len(writer1)), stdv(writer1)])


writer = csv.writer(open('simpsonswriters1.csv', 'wb'), delimiter=',')
for row in totalwriter:
	writer.writerow(row)
