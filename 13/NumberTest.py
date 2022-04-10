import re

# Regular Experssion RE, Regex------
# a. Meta Characters  . - ^ - $ - {} - |
# b.Sequences  \d - \D - \s - \S \w -\W
# c.Sets  [a-z] - [^] - [0-9] - [^0-9] -[a-zA -z]


# 0936 0397 0935 0938

mobile = '09382547896'
pattern = '^(0936|0937|0938|0935|0939)(\d{7}$)'
result = re.findall(pattern, mobile)

if __name__ == '__main__':
    if result:
        print('The mobile number is valid')
    else:
        print('Mobile number is not valid')
