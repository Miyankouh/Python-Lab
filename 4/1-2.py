# function definition
def is_palindrome(text):
    if text.lower() == text[::-1].lower():
    # if text.upper() == text[::-1].upper():
        return True
    else:
        return False

# function call
print(is_palindrome("Mom"))
print(is_palindrome("radar"))
print(is_palindrome("Aroma"))