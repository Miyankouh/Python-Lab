def print_books(list_of_books):
    for each_book in list_of_books:
        print(each_book)

my_books = ['book title 1', 'book title 2', 'book title 3']

def get_numbers():
    list_of_numbers = []
    for each_number in range(0, 10):
        list_of_numbers.append(each_number)
    return list_of_numbers

numbers = get_numbers()

if __name__ == '__main__':
    # print_books(my_books)
    print(numbers)