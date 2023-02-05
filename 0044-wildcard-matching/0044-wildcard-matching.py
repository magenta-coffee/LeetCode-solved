class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s = len(s)
        len_p = len(p)
        
        dp = [[False]*(len_p+1) for _ in range(len_s+1)]
        dp[0][0] = True
        
        for i in range(1, len_p+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]
        for i in range(1, len_s+1):
            for j in range(1, len_p+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
        return dp[len_s][len_p]
            