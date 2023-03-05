class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            second_tar = target - nums[i]
            if second_tar in nums:
                if nums.index(second_tar) != i:
                    return [i, nums.index(second_tar)]
        