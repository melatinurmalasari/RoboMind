def sum(*allNumber):
    total = 0
    for number in allNumber:
        total += number
    return total

def avg(*allNumber):
    hitung = 0
    for number in allNumber:
        hitung += 1
    return sum(*allNumber) / hitung

def max(*allNumber):
    max = allNumber[0]
    for number in allNumber:
        if(number > max):
            max = number
    return max

def min(*allNumber):
    min = allNumber[0]
    for number in allNumber:
        if(number < min):
            min = number
    return min 