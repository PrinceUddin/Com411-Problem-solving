song = '''  "Humpty Dumpty" sat on a wall,
Humpty Dumpty had a great, fall;
All the king's horses and all the king's men
Couldn't put Humpty together again.   '''

#print (set(song.lower().replace("\"","").replace("\'", "").replace(",","").split()))# len for counting words and set is for unique word
lista = song.lower().replace("\"","").replace("\'", "").replace(",","").split()
#print (type(lista))
#print (set(lista))
word_dict = {}

'''for word in lista:
  if word in word_dict:
    word_dict[word] += 1
  else:
    word_dict[word] = 1 '''

'''def sorting(dicta ={}):
  return dicta[1]'''

for item in lista:
  word_dict[item] = word_dict.get(item, 0) + 1

#print (word_dict)
print (dict(sorted(word_dict.items(), key = lambda  x: -x[1])))