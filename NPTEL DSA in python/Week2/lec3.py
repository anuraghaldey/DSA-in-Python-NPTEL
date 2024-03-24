# Lists
factors = [1, 2, 3, 4, 5]
names = ["Anurag", "Aditi", "Sanika"]
mixed = [3, True, "Anurag"]
print(mixed[1])  # here we get the value at mixed[1]
print(mixed[0:2])  # here we get the sublist

# Nested Lists
nested = [[2, 3, 4], [2, 3, [4, 5, [5, 6]]], ["Anurag", "Aditi"]]
print(nested[0])
print(nested[1])
print(nested[-1])
print(nested[2][1][3])


# Updating Lists
# we can update string directly
l1 = [34, 546, 8, 9, 0]
l1[1] = 78
print(l1)

# Lists are mutable eg:-
list1 = [1, 5, 7, 89]
list2 = list1
list1[0] = 2
print(list2[0])
print(list2[:])


# Copying Lists makes it immutable
list3 = [34, 45, 67, 88]
list4 = list3[:]
list3[0] = 3455
print(list4[0])

# Equality
ll1 = [2, 5, 6]
ll2 = [2, 5, 6]

print(ll1 == ll2)  # Bool returned
print(ll1 is ll2)  # checks if ll1 and ll2 pointing to the same list

x = [1, 2, 33]
y = x
print(x is y)

# Concatenation same like strings
lll1 = [1, 3, 4]
lll2 = [5, 6]
lll3 = lll1+lll2+[9]
print(lll3)
