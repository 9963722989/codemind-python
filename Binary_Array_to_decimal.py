import math

n = int(input())
a = list(map(int, input().split()))
c = n - 1
s = 0

for i in range(n):
    s += a[i] * int(math.pow(2, c))
    c -= 1

print(s)