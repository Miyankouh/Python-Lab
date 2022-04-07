# function definition
def print_numbers(_from, _to, _step):
    i = _from
    while i < _to:
        print(i)
        i += _step
    
    
    
# function call
_from = int(input('Enter from: '))
_to = int(input('Enter to: '))
_step = int(input('Enter step: '))

if __name__ == '__main__':
    print_numbers(_from, _to, _step)
