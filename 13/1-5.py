import re

# Regular Experssion RE, Regex
# c.Sets  [a-z] - [^] - [0-9] - [^0-9] -[a-zA -z]

text = 'Increase the desire to learn 0987654'

result_1 = re.findall('[a-l]', text)
result_2 = re.findall('[^a-l]', text)
result_3 = re.findall('[0-9]', text)
result_4 = re.findall('[^0-9]', text)
result_5 = re.findall('[a-zA -z]', text)

if __name__ == '__main__':
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)
