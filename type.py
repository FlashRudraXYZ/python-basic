 #arithmetic operators
a = 5
b = 2

print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) #a^b

#relational operators
a = 50
b = 20


print (a == b) #False
print (a != b) #True
print (a >= b) #True
print (a > b) #True
print (a <= b) #False
print (a<b) #False

#assignment operators
num = 10
num = num + 10 #10+10 => 20
print(num)

num = 10
num -=10
print("num:",num) #0

num = 10
num *= 5
print("num:",num) #50

num = 10
num /= 5
print("num:",num) #2

num = 10
num %= 5
print("num:",num) #0

num = 10
num **= 5
print("num:",num) #1,00,000

#logical operators
print(not False)
print(not True)

a = 50
a = 30
print(not False)
print(not(a > b))

val1 = True
val2 = True
print("ans operator:",val1 and val2)

val1 = True
val2 = False
print("ans operator:",val1 and val2)

print("and operator:", val1 and val2)

print("or operator:",val1 or val2)
