def romanize(tal):
    bord = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40], ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]
    result = ''

    if tal == 0:
        raise ValueError('can not encode zero')
    elif tal < 0:
        raise ValueError('can not encode negative number')

    for number in bord:
        while tal - bord[1] >= 0:
            tal -= bord[1]
            result += bord[0]


    return result