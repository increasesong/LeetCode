n = int(input())
s = list(map(int, input().split() ))

cps = list(map(lambda x: -x, s))
ans = 0
for item in s:
    if item in cps:
        ans+=1
ans=int(ans/2)
print(ans)
