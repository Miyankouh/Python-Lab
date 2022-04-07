# function definition
def is_list_empty(my_list):
    if my_list == []:
        print ("True")
    else:
        print ("False")

my_list = [1]
my_list2 = [1,2]

# is_list_empty(my_list)
# is_list_empty(my_list2)




# function definition
def is_list_empty(my_list):
    if len(my_list) == 0:
        return True
    else:
        return False

# function call
my_list = []
print(is_list_empty(my_list))