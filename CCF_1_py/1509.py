n = int(input())
s = list(map(int, input().split()))
ans = 1
for i in range(1,n):
    if s[i-1] != s[i]:
        ans+=1
print(ans)
