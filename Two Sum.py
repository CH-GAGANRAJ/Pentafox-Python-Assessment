l=list(map(int,input().strip().split()))
tar=int(input())
l.sort()
res=[]
p1=0
p2=len(l)-1
while p1<p2:
    if l[p1]+l[p2]==tar:
        res.append([p1,p2])
        break
    elif l[p1]+l[p2]>tar:
        p2-=1
    else:
        p1+=1
print(*res)
