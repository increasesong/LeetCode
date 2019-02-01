n = int(input())
s = list(map(int, input().split()))
s1 = list(map(lambda x: x+1, s))
ans=0
for item in s:
    if item in s1:
        ans+=1
print(int(ans))
        
