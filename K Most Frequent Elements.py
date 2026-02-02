l=list(map(int,input().strip().split()))
k=int(input())
res=[]
d={}
for i in range(len(l)):
    if l[i] in d:
        d[l[i]]+=1
    else:
        d.update({l[i]:1})
for i in d.keys():
    if d[i]>=k:
        res.append(i)
print(res)
