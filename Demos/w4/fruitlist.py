def getmefruits():
  fruits =[]
  print ("how many fruits would like to eneter?")
  n= int(input())
  for i in range(n):
    print("type in the next fruit:")
    fruits.append(input())
  print("your fruits are {}".format(fruits))
  return fruits

def get_fruits():
  fruits = ["apple","kiwi","banana", "mango","pinaple","pear"]
  fruits2 = getmefruits()
  print ("your fruits are:{}".format(fruits[1]))
#print only few items by slicing
  print(f"Sliced list: {fruits[0:5]}")

  print("the second list is {}".format(fruits2))
#print only few items using negative index
  print (f"Negative index : {fruits[-2:0:-1]}")
get_fruits()