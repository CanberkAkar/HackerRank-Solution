import numpy

n = int(input())

A = []
for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for _ in range(n):
    row = list(map(int, input().split()))
    B.append(row)

A = numpy.array(A)
B = numpy.array(B)

result = numpy.dot(A, B)
print(result)