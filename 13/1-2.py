import re

# Regular Experssion RE, Regex--
# d. Methods  -> findall() - search() - split(pattern- text- step) - sub(pattern- Replace - text- step)


# Things that can be done with regular words--
# Parsing
# Serching
# Serching & Replacing
# Splitting
# Validation


# findall = Only returns values
result = re.findall('an', "Tehran is the capital of Iran!")

# search = The first value = Displays values ​​in more detail
result_2 = re.search('an', "Tehran is the capital of Iran!")

# split = Break the words
result_3 = re.split("\s", "No device is required to view this code", 1)

# sub = Replace words with another word
result_4 = re.sub("\s", "***" , "Tehran is the capital of Iran!")


if __name__ == '__main__':
    print(result)
    print(result_2)
    print(result_3)
    print(result_4)
