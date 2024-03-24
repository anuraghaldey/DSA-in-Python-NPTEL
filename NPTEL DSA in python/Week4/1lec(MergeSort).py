
#Merge Sort-O(nlogn)-Consumes more space as we need to create a new array as c,inherently recursive
def merge(A, B):
    (C, m, n) = ([], len(A), len(B))
    (i, j) = (0, 0)

    while i < m and j < n:
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    while i < m:
        C.append(A[i])
        i += 1

    while j < n:
        C.append(B[j])
        j += 1

    return C

def mergesort(A):
    n=len(A)
    if (n == 1):
        return A
    mid=n//2
    l = mergesort(A[0:mid])
    r = mergesort(A[mid:n])

    return merge(l,r)

l=23,45,2,25,78,79,44,12

l=mergesort(l)


print(l)