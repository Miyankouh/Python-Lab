import re

# Regular Experssion RE, Regex--
# a. Meta Characters  . - ^ - $ - {} - |

text = '''Tehran is the capital of iran'''
text_2 = 'Hello, world'

result_1 = re.findall('.', text)
result_2 = re.findall('^Tehran', text)
result_3 = re.findall('iran$', text)
result_4 = re.findall('Hel{2}', text_2)
result_5 = re.findall('Tehran | is', text)


if __name__ == '__main__':
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)