class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_len = len(s)//2
        s_front = s[:s_len]
        s_back = s[s_len:]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        s_front_vowel = 0
        s_back_vowel = 0

        for i in range(s_len):
            if(s_front[i] in vowels):
                 s_front_vowel +=1
            if(s_back[i] in vowels):
                 s_back_vowel +=1

        if(s_front_vowel == s_back_vowel):
            return True
        else:
            return False 
