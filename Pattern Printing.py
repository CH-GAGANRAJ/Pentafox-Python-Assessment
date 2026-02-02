n=int(input())
p=1
for i in range(n+1):
    for j in range(i):
        print(p,end=' ')
        p+=1
    print()
