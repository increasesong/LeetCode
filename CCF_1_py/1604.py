n = int(input())
s = list(map(int, input().split() ))
ans = 0
for i in range(1,n-1):
    if abs(s[i-1]-s[i+1]) != abs(s[i-1]-s[i])+abs(s[i]-s[i+1]):
        ans+=1
print(ans)
