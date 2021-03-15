#while loop to print a countdown of number, from a user define value e.g. if user gives me 5, my code will print 5,4,3,2,1 BOOM

print ("what is the starting point?")
start = int (input())

while (start>=1):
  print(start)
  start-=5
print("BOOM!!!")