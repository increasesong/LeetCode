n = int(input())
s = list(map(int,input().split()))
dms = sorted(set(s))     #去重 sorted返回列表
max = 0
for item in dms:
    ct=s.count(item)
    if ct > max:
        max = ct
        ans = item
print(ans)
