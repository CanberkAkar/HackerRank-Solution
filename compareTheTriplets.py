
import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    aScore = 0 
    bScore = 0
    for i in range(3):
        if a[i] > b[i]: 
            aScore += 1
        elif a[i] < b[i]:
            bScore += 1
    
    comparison_array = [aScore, bScore]
    return comparison_array

a = [5, 6, 7]
b = [3, 6, 10]
print(compareTriplets(a, b)) 
a = [17, 28, 30]
b = [99, 16, 8]
print(compareTriplets(a, b))  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
