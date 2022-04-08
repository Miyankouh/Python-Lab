# debugging
# break point

# num1 = int(input("Please Enter Number 1: "))
# num2 = int(input("Please Enter Number 2: "))
# num3 = int(input("Please Enter Number 3: "))
# 
# result = max(num1,num2,num3)
# print("Max number between %d, %d and %d is %d" %(num1, num2,num3, result))



# for each_row in range(6):
    # print("*" * each_row)


# i = 5
# 
# while (i >= 1):
    # print("*" * i)
    # i-=1



# function definition
def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

# function call
print(is_palindrome("Mom"))
print(is_palindrome("radar"))
print(is_palindrome("Aroma"))