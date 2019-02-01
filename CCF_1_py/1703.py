n, k = map(int, input().split())
s = list(map(int, input().split() ))
ans = 0
temp = 0
i=0
while 1:
    temp=0
    while temp<k and i<n:
        temp+=s[i]
        i+=1
    ans+=1
    if i>=n:
        break
print(ans)
