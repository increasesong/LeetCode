n = int(input())
s = list(map(int, input().split() ))
ans= [0]*n      #[1]better
for i in range(n):
    for j in range(0,i+1):
        if s[i]==s[j]:
            ans[i]+=1
for item in ans:
    print(item, end=" ")
