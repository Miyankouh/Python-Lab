# iterating (for - while)
# 1. string "Iran"
# 2. range(int)


# numbers = range(1, 11)
# 
# for each_number in numbers:
    # print(each_number)

max = 0

while True:
    value = input("please enter a number: ")
    if value == "stop":
        break
    else:
        num = int(value)
        if num> max:
            max = num

print(f"max number is {max}")