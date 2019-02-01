s = list(map(int, input().split() ))
ans=0
i=0
last=1
n=0
while 1 :
    if s[i] == 0:
        break
    if s[i] == 1:
        ans+=1
        n=0
    if s[i] == 2:
        n+=1
        if last == 1:
            ans+=2
        if last == 2:
            ans+=2*n
    last=s[i]
    i+=1
print(ans)
