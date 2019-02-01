n = int(input())
s = list(map(int, input().split()))
ans = 10000
s.sort()
for i in range(1,n):
    temp=s[i]-s[i-1]
    if temp < ans:
        ans=temp
print(ans)
