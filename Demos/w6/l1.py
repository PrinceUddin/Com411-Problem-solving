phonebook = {}

while True:
  name = input("enter the name:")
  number = input("enter the number:")# did not use int cause if we use int we can' t use country code like +44 or +39
  phonebook[name] = number
  if input("Type x to stop") == 'x':
    break

#print(phonebook)    
# if i want to call a particular name exsist in phone book
def calling(n, book = {}):
  print(f"calling {n} with a phone number {book[n]}")

  phonebook["taked" =]

calling("prince",phonebook)