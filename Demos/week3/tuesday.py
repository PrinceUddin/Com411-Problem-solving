#print ("The letter '@' in ASCII table is represented by {}".format(ord('@')))

#print ("The Character '@' in ASCII table is represented by hexadecimal number {}".format(hex(ord('@'))))

#defining my own function to calculate area of triangle

def calculate_area(h=10,b=5):
  area = 0.5*h*b
  return area
#h = 10
#b = 5
#print("enter height and base of triangle")
#h = float(input())
#b = float(input())


#call for the function
#calculate_area(h,b)

def run ():
  x = calculate_area(4) 
  x += 1
  print (f"the are of triangle is {x}")
  run()