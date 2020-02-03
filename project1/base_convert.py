
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    if num == 0:
        return str(num)
    if num % b >= 10:
        newnum = chr(num % b + 55)
    else:
        newnum = num % b
    if num//b != 0:
        return '{}{}'.format(convert(num//b,b), newnum)
    else:
        return newnum

print(convert(0, 0))