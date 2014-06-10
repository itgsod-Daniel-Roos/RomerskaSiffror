def romanize(tal):
    #Takes a number and transforms it into its roman counterpart.
    #For example;
    #romanize(200)
    #>>> "CC"

    table = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40], ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]
    result = ''                                             #Arrays in arrays makes up the table of numberconverters.

    if tal == 0:
        raise ValueError('can not encode zero')
    elif tal < 0:
        raise ValueError('can not encode negative number')

    for number in table:                                     #For each value in the table, the loop checks - top to down -
        while tal - number[1] >= 0:                          #if the current value of the tableindex can be entered without
            tal -= number[1]                                 #the original input going into negative. When the value eventually
            result += number[0]                              #is 0, the loop stops.


    return result

def addition(x, y):
    return x + y