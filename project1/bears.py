def bears(n):
    """A True return value means that it is possible to win
     the bear game by starting with n bears. A False return value means
     that it is not possible to win the bear game by starting with n
     bears."""
    if n == 42:
        return True
    if n <42:
        return False
    if n % 5 == 0:
        number= n-42
        if bears(number):
            return True
    if n % 3 == 0 or n % 4 == 0:
        if len(str(n)) >= 2 and int(str(n)[-1]) !=0 and int(str(n)[-2]) != 0:
            number=n-(int(str(n)[-1]) * int(str(n)[-2]))
            if bears(number):
                return True
    if n % 2 == 0:
        number=n // 2
        if bears(number):
            return True
    return False
