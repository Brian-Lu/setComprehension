def union(A, B):
    return [x for x in A if x not in B] + [x for x in B]

def intersection(A, B):
    return [x for x in A if x in B]

def setDifference(U, A):
    return [x for x in U if x not in A]

def symmetricDifference(A, B):
    return setDifference(union(A, B), intersection(A, B))

def cartesianProduct(A, B):
    return [(a, b) for a in A for b in B]

setA = [1, 2, 3, 4]
setB = [2, 4, 5, 7]

print union(setA, setB)
print intersection(setA, setB)
print setDifference(setA, setB)
print symmetricDifference(setA, setB)
print cartesianProduct(setA, setB)