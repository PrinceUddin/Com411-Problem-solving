#lets talk diffrent type of delattr
print("what is your name?")
#gooing to assain a variable. variable is a container, ehich can store for us in the memory (sting, inger, float, bool)
name = input()
#name=5
#print (type(name))
print ("what is your age?")
age = int(input())
#print(type(age))
print("what is your bank balance?")
balance = float(input())

print ("WELCOME {}. you are said to be {} years old. your bank balance is {:.2f}.". format (name, age, balance))