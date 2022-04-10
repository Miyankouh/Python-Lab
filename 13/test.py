import re

# Regular Experssion RE, Regex------
# a. Meta Characters  . - ^ - $ - {} - |
# b.Sequences  \d - \D - \s - \S \w -\W
# c.Sets  [a-z] - [^] - [0-9] - [^0-9] -[a-zA -z]


# email 

# behroz@gmail.com
# .+\@.+\..+

email = r'templates@gmail.com'
pattern = '.+\@.+\..+'

result = re.findall(pattern, email)


if __name__ == '__main__':
    if result:
        print('your email address is valid')