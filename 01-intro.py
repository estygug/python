
"""
1

x=input("enter your age please ")
age=12*int(x)
print(f"your mounthly age is {age}")

2

x=input("enter your  mounthly age please ")
age=int(int(x)/12)
print(f"your mounthly age is {age}")

3

x = input("enter number please ")
boom = int(x)%7
if boom == 0:
    print("boom")
print("end")
4

x = input("enter number please ")
boom = int(x)%7
if boom == 0 or '7' in x :
    print("boom")
print("end")
5

a=int(input("enter first num"))
b=int(input("enter second num"))
c=int(input("enter third num"))
print(max([a, b, c]))
6
a1 = int(input("enter a1 num"))
d = int(input("enter d num"))
n = int(input("enter an num"))
sum1 = (((d*(n-1))+(2*a1))*n)/2
print({sum1})
11

x = input("enter number please ")
check = int(x)%2
if check == 0  :
    print("even")
else:
    print("odd")
22

a=int(input("enter first num"))
b=int(input("enter second num"))
c=int(input("enter third num"))
if a+b==c or b+c==a or a+c==b:
    print("true")
else:
    print("false")
33

num = int(input("enter number please "))
string="*"
for x in range(num):
  print({string})
  string=string+"*"
44

num = int(input("enter number please "))
string="*"
sum1 = (2*num)-1
for x in range(num):
  a = string.center(sum1, " ")
  print({a})
  string="*"+string+"*"
  55
"""
def read_until_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("it wasn't a number!!!")
            pass
num1 = read_until_number("enter number please ")
num2 = read_until_number("enter number please ")
while True:
     operator = input("enter operator please ")
     try:
         if operator =='+' :
             sum= num1+num2
             break
         elif operator == '-':
             sum= num1-num2
             break
         elif operator == '*':
             sum= num1*num2
             break
         elif operator == '/':
             sum= num1/num2
             break
     except ValueError:
          print("it wasn't a operator!!!")
print(sum)

