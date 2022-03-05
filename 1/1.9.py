# Operators

# 1. Arithmetic Operators  # عملگرد های ریاضی

# 2. Assignment Operators  # عملگردهای انتصابی   

# 3. Comparison Operators  # عملگردهای مقایسه ای


a = 100

b = 3

result = a + b
# print("The addition of" + a + "and" + b + "is" + result) # type error

print("The addition of %d and %d is %d" % (a, b, result))



result = a - b
print("The subtraction of %d and %d is %d" % (a, b, result)) 


result = a * b
print("The multiplcation of %d and %d is %d" % (a, b, result)) 


result = a / b
print("The division of %d and %d is %d" % (a, b, result)) 


result = a % b
print("The modulus of %d and %d is %d" % (a, b, result)) 


result = a ** b
print("The exponent of %d and %d is %d" % (a, b, result)) 


result = a // b
print("The floor division of %d and %d is %d" % (a, b, result)) 


a = 10
a += 3

print(a)

#--------------------------------------------------------------------------------------------------------------------------
# Operator					Shorthand form	What It Does
# --------------------------------------------------
# + 	Addition 			+=				Add two operands
# - 	Subtraction 		-=				Subtract right operand from the left 
# * 	Multiplication 		*=				Multiply two operands
# / 	Division 			/=				Divides the operand on left by the one on right.
# % 	Modulus 			%=				Divides the operand on left by the one on right and returns	remainder
# ** 	Exponent 			**=				left operand raised to the power of right
# // 	Floor division 		//=				Performs just like the / division operator, but truncates the result at the decimal point
#--------------------------------------------------------------------------------------------------------------------------
