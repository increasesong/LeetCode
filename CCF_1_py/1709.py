n = int(input())
ans = 0
while n >= 50:
    n-=50
    ans+=7
while n >= 30:
    n-=30
    ans+=4
while n >= 10 :
    n-=10
    ans+=1
print(ans)
