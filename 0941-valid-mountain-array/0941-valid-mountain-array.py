class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        peek = arr[0]
        peek_index = 0
        for p in range(0, len(arr)):
            if arr[p] < peek:
                break
            peek = arr[p]
            peek_index = p

        for i in range(0,peek_index):
            if (arr[i] >= peek) or (arr[i] >= arr[i+1]):
                return False
            else:
                continue

        length = len(arr)
        if(peek_index==0 or peek_index==len(arr)-1):
            return False

        for i in range(peek_index+1,length):
            if (arr[i] >= peek) or (arr[i-1] <= arr[i]):
                return False
            else:
                continue
        return True
