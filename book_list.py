"""
Program: book_list.py
Author: Travis Wagner
Creation Date: 4/7/2022
Description: Asks user to enter a number of books along with the names and prices of those books.
It lists the books in a table, adds the prices, and averages the prices.
a table,
"""
import pyinputplus as pyip


def main():  # call functions and save results under key variable names.
    print('This program summarizes a book list.')
    try:  # generic exception handling - turn off during development
        num_books, price_list, book_list = inputs()
        total, average = processing(price_list)
        outputs(num_books, price_list, total, average, book_list)
        restart = pyip.inputYesNo(prompt='Need more books? Enter yes or no: ')# restart feature
        if restart == 'yes':
            main()
        elif restart == 'no':
            print('Thanks for using the program.')
    except Exception as err:  # turn off during development
        print(err)  # turn off during development


def inputs():  # collect info needed from the user.  # user sets the list length/ repetitions of the for loop
    num_books = pyip.inputNum(prompt='Enter the number of books that you need ')  # asks for number of books
    price_list = []  # create list to save prices
    book_list = []  # list for books entered
    for index in range(num_books):  # for loop runs user-specified number of times & collects info on each book
        book_name = input(f'Enter the name of book #{index + 1}: ')
        book_list.append(book_name)  # adds books entered to list
        book_cost = pyip.inputFloat(prompt=f'Enter the cost of book #{index + 1}, ' # asks for cost of books
                                           f'to the nearest dollar: $', max=100)
        price_list.append(book_cost)  # build price list
    return num_books, price_list, book_list


def processing(price_list):  # use the list to calculate summary data
    total = sum(price_list)
    average = round(total / len(price_list), 2)
    return total, average


def outputs(num_books, price_list, total, average, book_list):  # table displaying name, price, total, and average
    print(f'Info on {num_books} Books Needed')
    print(f'{"Books ":<10}{"Price":>23}')
    for index in range(len(price_list)):
        print('{:<24}{:>2}{:>5}'.format(book_list[index], '$', f'{price_list[index]:>8.2f}'))
    print(f'{"Total":<24} ${total:>8.2f}')
    print(f'{"Average":<24} ${average:>8.2f}')


main()
