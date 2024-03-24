
def g(m, n):
    res = 0
    while m >= n:
        (res, m) = (res+1, m/n)
    return (res)


def ans():

    for i in range(2, 375):
        if g(375, i) == 4:
            return i

    return -1


print(ans())
