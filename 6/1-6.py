# function definition
def print_numbers(_from, _to, _step):
    for num in range(_from, _to, _step):
        print(num)

# function call
_from = int(input('Enter from: '))
_to = int(input('Enter to: '))
_step = int(input('Enter step: '))

if __name__ == '__main__':
    print_numbers(_from, _to, _step)
