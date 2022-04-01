# function definition
def are_strings_equal(str1, str2, is_case_sensitive=False):
    if is_case_sensitive == True:
        return str1 == str2
    else:
        return str1.lower() == str2.lower()

print(are_strings_equal("TEHRAN", "tehran"))
print(are_strings_equal("TEHRAN", "tehran", True))


def f(t1, t2):
    if t1.lower() == t2.lower():
        return True
    else:
        return False

print(f("name", "NAME"))