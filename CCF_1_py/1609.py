n = int(input())
s = list(map(int, input().split() ))
ans = 0
for i in range(1,n):
    temp = abs(s[i]-s[i-1])
    if temp > ans:
        ans = temp
print(ans)
