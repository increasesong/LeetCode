class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        n=0
        for i in range(0,len(nums)):
            if nums[i] != nums[n]:
                n+=1
                nums[n]=nums[i]
        return n+1;