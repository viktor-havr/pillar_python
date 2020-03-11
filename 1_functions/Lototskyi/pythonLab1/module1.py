'''
Fibonacci`s numbers
Hello to my first function

It will help you to calculate needed element of Fibonacci`s numbers

Example:
    module1.fibNumb(7) - will return 13

Attributes:
   def fibNumb(int)
        Has only one attribute - Fibonacci sequence number you want to get

Todo:
    * change funtion to not be recursive

'''


def fibNumb(number):
    if number > 0:
        if (number == 1) | (number == 2):
            return 1
        else:
            return fibNumb(number - 1) + fibNumb(number - 2)
    else:
        print("input error")


