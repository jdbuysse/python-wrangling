
import numpy as np

# complete this function so that it returns
# the square of the number passed to it

def square(number):
    return int(number)*int(number)

# complete this function so that it returns
# the result of float division of 
# number 1 / number 2
    
def division_float(number1,number2):
    if number2 == 0:
        return 'nan'
    return number1/number2
    
# complete this function so that it returns
# the first element of a list passed to it
def first_from_list(list):
    if list == []:
        return 'nan'
    return list[0]

# return the value of pi from the numpy library

def pi():
    return np.pi










