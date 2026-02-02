l=input().strip().split()
s=''
n=float('inf')
for i in l:
    n=min(len(i),n)
i=0
while i<n:
    c=0
    p=l[0][i]
    for j in l:
        if j[i]==p:
            c+=1
    if c==len(l):
        s+=l[0][i]
    i+=1
print(s)