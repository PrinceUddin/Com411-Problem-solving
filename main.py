


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