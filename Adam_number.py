n=int(input())
m=n*n
t=n
rev=0
while(t!=0):
    r=t%10
    rev=rev*10+r
    t=t//10
s=rev*rev
rev1=0
while(s!=0):
    r1=s%10
    rev1=rev1*10+r1
    s=s//10
print(m==rev1)

