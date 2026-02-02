n=int(input())
p=0
a=len(str(n))
a=10**(a-1)
while n:
    r=n%10
    p+=(r)*a
    n=n//10
    a=a//10
print(p)