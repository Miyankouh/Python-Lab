# function definition
def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

# function call 
print(is_palindrome('bob'))
print(is_palindrome('new'))
print(is_palindrome('boob'))



