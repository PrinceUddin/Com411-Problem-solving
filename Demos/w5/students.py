#program that imitate a small database in the sanse that it can:
#inster new student and their mar
#keep continually add stufdents
#print out students name and their work
#avarage mark of all student
#find the maximum among all student

'''all_student = [("gray",67),("uzma",82), ("mihai",76)]
print(all_student[1][0])'''

def generate_stds():
  print("Enter the name of student:")
  name = input()
  print("Enter the student grade:")
  grade = int(input())
  return name, grade

'''t = generate_stds()
print (t)'''

def all_stds():
  all_students = []
  while True:
    all_students.append(generate_stds())
    print("To stop adding students, type 0")
    x= input()
    if x =='0':
      break # break of while loop
  return all_students

def print_students(lista):
  for std in lista:
    print(f"{std[0]} earned a grade {std[1]}")

#print_students(all_stds())

def avr_mark(lista):
  total=0
  for std in lista:
    total += std[1]
  return total/len(lista)

print(avr_mark(all_stds()))