#trying to compose a program finding prime number
def isPrime(x):
  for i in range(2,x):
    if x%i == 0:
      return False
  return True

def findPrime(beginning,  finish):
  for j  in range (beginning,finish):
    if isPrime(j):
      return j
    
def encrypt():
  print("provide two integers")
  x = int (input())
  y = int (input())
  prime1= findPrime(x,y)

  print("provide two more integers")
  x = int (input())
  y = int (input())
  prime2= findPrime(x,y)
  return prime1*prime2

print(encrypt(), encrypt())

#print(f"The prime between {x} and {y} is {findPrime(x,y)}")
#print("what is the number?")
#x=int(input())
#if isPrime(x):
#  print(f"the number{x} is prime!")
#else:
#  print("the number is not prime!")
