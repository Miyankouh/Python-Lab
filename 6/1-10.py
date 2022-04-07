import random

# function definition
def get_random_item(my_list):
    ran_index = random.randint(0,len(my_list)-1)
    run_item = my_list[ran_index]
    return run_item

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(get_random_item(my_list))

