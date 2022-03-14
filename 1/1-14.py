#-------------------------------------------------------------------------------------------
#   name       			description
#-------------------------------------------------------------------------------------------
#   len()               Returns the number of characters in a string
#   capitalize()        Converts the first character of a string to capital letter
#   count()             Returns the number of occurrences of a substring in the given string
#   lower()             Converts a string into lower case
#   upper()	            Converts a string into upper case
#   isspace()           Returns True if all characters in the string are whitespaces
#   replace()           Replaces all or part of a string with another string
#   isdigit()           Returns True if the string consists of digits only
#-------------------------------------------------------------------------------------------

# Function
my_name = "newman"
result = len(my_name)
print("%s has %d characters" %(my_name, result))


# Method
my_name2 = "newman"
result = my_name.capitalize()
print(result)


# Method
quote = """ if you really want to do something youll find away
    if you dont, youll find an excuse"""

# Method
result = quote.count("you")
print("the substring '%s' is repeated %d tims in the string " %("you", result))


# Method
# print(input("enter your first name: ").upper())
# print(input("enter your last name(upper case): ").lower())


# Method
result2 = " a ".isspace() 
print(result2)



quote2 = "All progres takes place outside the comfort zone."
quote3 = quote2.replace("progres", "progress")
print(quote3)



print("12345678901".isdigit())
