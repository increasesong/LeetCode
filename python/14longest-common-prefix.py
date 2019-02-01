strs=["flower","flow","flight"]
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    a=100000000
    loc=0
    for item in strs:
        l=len(item)
        if a > l :
            a=l
            loc=strs.index(item)
    ans=''
    for i in range(0, a):
        same=strs[loc][i]
        for item in strs:
            if item[i] != same:
                return ans
        ans=ans+same
    return ans
print(longestCommonPrefix(strs))
