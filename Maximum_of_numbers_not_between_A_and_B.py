n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
m = a[0]

for i in range(n):
    if m < a[i] and not (a[i] >= b and a[i] <= c):
        m = a[i]

if m == a[0]:
    print("-1")
else:
    print(m)