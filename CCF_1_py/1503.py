n, m = map(int, input().split())
r=[]
for i in range(n):
    a=list(map(int, input().split()))
    r.append(a)
for row in range(m):
    for col in range(n):
        print(r[col][m-1-row], end=' ')
    print()
