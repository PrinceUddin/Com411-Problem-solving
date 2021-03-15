



print  ("please choose and option from the menu:\n\n1-Nice message\n2-Area of a rectangle\n3-area of triangle\n4-Times table")

option = int(input())

if option == 1:
  print("Today will be a good day!")
elif option ==2:
  print ("enter the lenght of the rectangle:")
  l = int(input())
  print ("enter the wide of rectangle")
  w = int (input())
  area = w*l
  print("2The area of this rectangle was {}".format(area))
elif option == 3:
  print ("enter the base of the triangle")
  b = float(input())
  print ("enter the hight of the triangle")
  h = float(input())
  area = 0.5*b*h
  print ("The area of triangle was {:.2f}".format(area))
elif option == 4:
  print("what number would like to see Times table for?")
  n = int(input())
  for i in range(1,100,1):
    print("{}x{}={}".format(n,i,n*i))
else:
  print("there is no such option. go to specserver!")
=======
#while loop (and also FOR loop) can be used to have a repetition of a procedure in our code

print("how many time print the simble?")
x = int(input()) # x=3

#i is a counter - it keeps trak of how many times we went through the Loop
i = 0

while i < x:# condition for repeating the code - as long as i lower than x
  print("\u27bd", i)
  i = i+1 # new value of the counter is one more than it used to be

print ("we left the loop")
