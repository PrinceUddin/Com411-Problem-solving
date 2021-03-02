#while loop (and also FOR loop) can be used to have a repetition of a procedure in our code

print("how many time print the simble?")
x = int(input()) # x=3

#i is a counter - it keeps trak of how many times we went through the Loop
i = 0

while i < x:# condition for repeating the code - as long as i lower than x
  print("\u27bd", i)
  i = i+1 # new value of the counter is one more than it used to be

print ("we left the loop")