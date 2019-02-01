n = int(input())
s = list(map(int, input().split() ))
ans = -1
s.sort()
mid = n // 2
h = n // 2
t = n // 2 
while h>0 and s[h-1]==s[mid]:
    h-=1
while t<n-1 and s[t+1]==s[mid]:
    t+=1
if h == (n-t-1):
    ans=s[mid]
print(ans)
