# Conditional
x = 1
y = 2

if x == 1:
    x = 2
elif x == 2:
    x = 1
else:
    x = 45


print(x)


# Loops
a = 1
b = 2
for i in range(1, 5):
    a = a*i
    b = b+i

print(a+b)

# Checking for factors of n
n = 8
list1 = []
for i in range(2, n):
    if (n % i == 0):
        list1 = list1 + [i]

print(list1)
