class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        def backtrack(root=0):
            if root == len_nums:
                result.append(nums[:])
            for i in range(root, len_nums):
                nums[root], nums[i] = nums[i], nums[root]
                backtrack(root + 1)
                nums[root], nums[i] = nums[i], nums[root]
                
        len_nums = len(nums)        
        backtrack()
        return result
                