my_list = [10, 20]
my_list2 = [my_list, 30, 40, 50]

# for item in my_list:
#     print(item)

# i = 0
# while i < len(my_list):
#   print(my_list[i])
#   i += 1


for each_item in my_list2:
    if type(each_item)==list:
        for inner_item in each_item:
            print(inner_item)
    else:
        print(each_item)