#while loop to print a countdown of number, from a user define value e.g. if user gives me 5, my code will print 5,4,3,2,1 BOOM

print ("what is the starting point?")
start = int (input())
start_copy = start


while (start>=1): #condition that needs to be satisfaction for loop to continue
  print(start)
  start-=5 #modification to counter variable to avoid infinity loop
print("BOOM!!!")


for counter in range(start_copy, 1, -1):
  print(counter)
print("BOOM!!!")