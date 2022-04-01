# function definition
def is_pin_valid(pin_code):
    if pin_code.isdigit() == True:
        if len(pin_code) == 4 or len(pin_code) == 6:
            return True
    return False

print(is_pin_valid("newpass"))
print(is_pin_valid("1234"))
print(is_pin_valid("125874"))
print(is_pin_valid("1258744578"))
