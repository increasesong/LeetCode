r, y, g = map(int, input().split())
n = int(input())
ans=0
for i in range(n):
    a=list(map(int, input().split()))
    if a[0]==3:
        continue
    if a[0]==2:
        ans+=r
    ans+=a[1]
print(ans)
