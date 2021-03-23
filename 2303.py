def student():
  print("enetr your name:")
  name = input()
  print("what is your age?")
  age = int(input())
  print("do you have a dog?")
  dog = input()
  if dog == "yes":
    dog_bool = True
  else:
    dog_bool = False
  return  name,age,dog_bool


'''  
person = ("piotr", "67", True)

print(person)

#access elements via index - just
print (person[1])
if person[2]:
  print("yay - you have a doggo!")
else:
  print("no doggo no fun!")

print("which itemto print")
n = int (input())
if n < len(person):
  print(person[n-1])

#cannot modify (mutate) AttributeError
#person [0] = "peter"
#print(person)

print(person + (2000, "black"))
'''
#print(student())

print("how many students to generate?")
n = int(input())# if user input 5
count = 0 # keeps track how many times repetetions we have done
all_students = []
while( count <n):
  tuplex = student()
  all_students .append(tuplex)
  count+=1
print(all_students)

