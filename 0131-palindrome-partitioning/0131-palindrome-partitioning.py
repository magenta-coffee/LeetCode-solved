class Solution:
    def checkPalindrome(self, str, startIndex, lastIndex):
        while startIndex <= lastIndex:
            if str[startIndex] != str[lastIndex]:
                return False
            startIndex += 1
            lastIndex -= 1
        return True

    def palindromePartition(self, index, ds, output, str):
        if index == len(str):
            output.append(ds[:])
            return
        for i in range(index, len(str)):
            if self.checkPalindrome(str, index, i):
                ds.append(str[index:i+1])
                self.palindromePartition(i+1, ds, output, str)
                ds.pop()

    def partition(self, s: str) -> List[List[str]]:
        output = []
        ds = []
        self.palindromePartition(0, ds, output, s)
        return output
