#writing a new file
'''file = open("gaga.txt","w")
file.write("This is an example \n it makes no sense\n because i run out of ideas!")
file.close()'''

'''#for reading from file
file = open("gaga.txt")
print (file.read())
file.close()'''

'''#to reat paeticular line
file = open("gaga.txt")
print (file.readlines()[1])
file.close()'''

file = open("gaga.txt")
print file.readlines()
print (f"Line:{i}", end = )
file.close()