import random

sides = int(input('how many side dose the dice have? '))
run_num = random.randint(1, sides)

my_list = []
for _ in range(10):
    my_list.append(random.randint(0,100))


if __name__ == '__main__':
    # print(run_num)
    print(my_list)