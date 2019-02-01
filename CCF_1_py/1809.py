n = int(input())
s = list(map(int, input().split()) )
ans = [1]*n
ans[0]=(s[1]+s[0])//2
ans[n-1]=(s[n-1]+s[n-2])//2
for i in range(1,n-1):
    ans[i]=(s[i]+s[i-1]+s[i+1])//3
for item in ans:
    print(item, end=' ')
