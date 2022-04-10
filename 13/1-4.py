import re

# Regular Experssion RE, Regex
# b.Sequences  \d - \D - \s - \S \w -\W

text = 'A world full of life'
text_2 = '1004'
text_3 = 'Welcome! 123 _ * @ #|'

result_1 = re.findall('\D', text)
result_2 = re.findall('\d', text_2)

result_3 = re.findall('\s', text)
result_4 = re.findall('\S', text)

result_5 = re.findall('\w', text_3)
result_6 = re.findall('\W', text_3)


if __name__ == '__main__':
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)
    print(result_6)
