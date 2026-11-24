import sys
def largest(a,b,c):
  print("Enter Three Numbers:")
  
  a=int(input("Enter a: "))
  b=int(input("Enter b: "))
  c=int(input("Enter c: "))

if a>b and a>c:
 print("a is largest:",a)

elif b>a and b>c:
 print("b is largest:",b)

elif c>a and c>b:
 print("c is largest:",c)

else:
 print("Two are more numbers are equal:")

largest()
