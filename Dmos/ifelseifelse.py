# if statement
print ("whats is you name?")
n = input()
#print("do you have a dog?(type ture or false)")
#dog = bool(input())
#dog = input()

# bool is boolean datatype only use ture or false statement

if len (n)>=9 # allow lenght of exactly 9 and greater :
  print ("you have a very long name!")
  print("your nam contain {} letter". format(len(n)))
elif len(n)>6:
  print ("yor nam eis bit long. consider a nickname")
elif len (n)<3:
    print ("yor name very short")
else:
  print("your name is quite okay")
  print("your nam contain {} letter". format(len(n)))

print("this is the end of the program!")