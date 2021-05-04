
# reading from csv file
'''import csv

with open("fold1/fold2/data.csv") as d:
  reader = csv.reader(d,delimiter = ",", quotechar = "'")
  for row in reader:
    print(row)'''

#writing in file csv

f = open ("fold1/fold2/data.csv", "w")

lista = ["name","mark", "tel"]

for i in lista:
  f.write(i)
  f.write(",")