

def threesquares(n):
    ans = n
    for a in range(0, n):
        for b in range(0, n):
            if (ans == (pow(4, a)*(8*b+7))):
                return False

    return True


print(threesquares(28))


def repfree(s):
    s1 = ''.join(sorted(s))
    for i in range(1, len(s1)):
        if (s1[i] == s1[i-1]):
            return False
    return True


print(repfree("abracadabra"))


def hillvalley(l):
    if (len(l) <= 2):
        return False

    (h, v) = (False, False)
    if (l[1] > l[0]):
        h = True
    else:
        v = True

    if (h):
        n = 1
        while (l[n] > l[n-1]):
            n = n+1
        if (n == len(l)-1):
            return False

        for i in range(n+1, len(l)):
            if (l[i] > l[i-1]):
                return False
        return True
    else:
        n = 1
        while (l[n] < l[n-1] and n < len(l)-1):
            n = n+1
        if (n == len(l)-1):
            return False

        for i in range(n+1, len(l)):
            if (l[i] < l[i-1]):
                return False
        return True


print(hillvalley([5, 4, 3, 2, 1, 0, -1, -2, -3]))
