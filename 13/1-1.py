import re

# Regular Experssion RE, Regex
# a. Meta Characters
# b.Sequences
# c.Sets

# d.Methods

if 'code' in 'code academy':
    print('yes!')

pattern = 'code'
text = 'code academy'

result = re.match(pattern, text)
print(result)