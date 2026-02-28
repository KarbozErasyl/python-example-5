#variable <operator>= value
my_var = 10
my_var += 5

print(my_var) # 15

my_var = 10
my_var = my_var + 5

print(my_var) # 15

count = 14
count -= 3

print(count) # 11

product = 65
product *= 7

print(product) # 455

price = 100
price /= 4

print(price) # 25.0

total_pages = 23
total_pages //= 5

print(total_pages) # 4

bits = 35
bits %= 2

print(bits) # 1

power = 2
power **= 3

print(power) # 8

greet = 'Hello'
greet += ' World'

print(greet) # Hello World

greet = 'Hello'
greet *= 3

print(greet) # HelloHelloHello

greet = 'Hello'
greet -= ' World'

print(greet) # TypeError: unsupported operand type(s) for -=: 'str' and 'str'


greet = 'Hello'
greet /= 'World'

print(greet) # TypeError: unsupported operand type(s) for /=: 'str' and 'str' 

my_var = 5

print(+my_var)   # 5
print(++my_var)  # 5
print(+++my_var) # 5

my_var += 1

print(my_var) # 6

print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True

#Operator 	Name 	Description
#== 	Equal 	Checks if two values are equal
#!= 	Not equal 	Checks if two values are not equal
#> 	Greater than 	Checks if the value on the left is greater than the value on the right
#< 	Less than 	Checks if the value on the left is less than the value on the right
#>= 	Greater than or equal 	Checks if the value on the left is greater than or equal to the value on the right
#<= 	Less than or equal 	Checks if the value on the left is less than or equal to the value on the right

age = 18

if age >= 18:
    print('You are an adult') # You are an adult

age = 18

if age >= 18:
print('You are an adult') # IndentationError: expected an indented block after 'if' statement on line 3

age = 12

if age >= 18:
    print('You are an adult') # Nothing shows up in the terminal

