class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        diffs = []
        worddict = {
            'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8,
            'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17,
            's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25
        }
        
        for i in range(len(words)):
            diff = []
            for j in range(len(words[i])-1):
                diff.append(worddict[words[i][j+1]] - worddict[words[i][j]])
            diffs.append(diff)

        first = diffs[0]
        second = diffs[1]
        for j in range(2,len(diffs)):
            if (first == second):
                if diffs[j] != first:
                    return words[j]
            else:
                if(first == diffs[j]):
                    return words[1]
                else:
                    return words[0]
            