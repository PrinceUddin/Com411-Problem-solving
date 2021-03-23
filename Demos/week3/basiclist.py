#define an empty list
fruits =[]

#Define a list with items

vegetables = ["carrot", "peas"]

#Add items to the list
fruits.append("Apple")
fruits.append("Banana")
fruits.append("Tommatoes")
fruits.append("Banana")
print(fruits)

#remove an itemn from list
fruits.remove("Banana")
print(fruits)
#remove item by index
del fruits[1]
print(fruits)

#insert a value not in the print
fruits.insert(1, "Pinaple")
print(fruits)
#Access single element
print(fruits[0])