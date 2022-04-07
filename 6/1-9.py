# function definition first
def append_lists(l_1, l_2):
    return l_1 + l_2

# function definition tow
def append_list(list1, list2):
    for item in list2:
        list1.append(item)
    return list1

list_1 = [1, 2, 3]
list_2 = [4, 5]

if __name__ == '__main__':
    print(append_lists(list_1, list_2))
    print(append_list(list_1, list_2))
