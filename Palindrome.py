s=input()
a=''
for i in s:
    if i in ',.;:!@#$%^&*()[]{}':
        continue
    elif i==' ':
        continue
    else:
        p=i.lower()
        a+=p
if a==a[::-1]:
    print("true")
else:
    print("flase")