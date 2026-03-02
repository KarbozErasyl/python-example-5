is_citizen = True
age = 25
if is_citizen:
	if age >= 18:
		print('You are eligible to vote') #You are eligible to vote
else:
	print('You are not eligible to vote')


print(bool(False)) #False
print(bool(0)) #False
print(bool('')) #False

print(bool(True)) #True
print(bool(1)) #True
print(bool('Hello')) #True


is_citizen = True
age = 25

print(is_citizen and age) #25