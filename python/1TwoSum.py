def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashmap = {}
    for i, num in enumerate(nums):
        rest = target - num
        if rest in hashmap:
            return [hashmap[rest], i]
        hashmap[num] = i
    return None



nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
