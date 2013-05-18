from imdb import IMDb
import csv


ia = IMDb()
m = ia.get_movie('0096697') #simpsons imdb id (without the tt)
ia.update(m, 'episodes')
totallist = []
totallist.append(['season','episode','title','votes','rating', 'writers'])

for i in range(1,24 + 1):
	if i == 24:
		for j in range(1,20):
			ia.update(m['episodes'][i][j])
			for k in range(4,len(m['episodes'][i][j]['writer'])):
				totallist.append([i,j,m['episodes'][i][j]['title'],m['episodes'][i][j]['votes'],m['episodes'][i][j]['rating'],m['episodes'][i][j]['writer'][k]['name']])
	else:
		for j in range(1,len(m['episodes'][i])):
			ia.update(m['episodes'][i][j])
			for k in range(4,len(m['episodes'][i][j]['writer'])):
				totallist.append([i,j,m['episodes'][i][j]['title'],m['episodes'][i][j]['votes'],m['episodes'][i][j]['rating'],m['episodes'][i][j]['writer'][k]['name']])


writer = csv.writer(open('simpsons3.csv', 'wb'), delimiter=',')
for row in totallist:
	writer.writerow(row)

