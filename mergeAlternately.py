class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = []
        len1,len2 = len(word1),len(word2)
        i, j = 0, 0
        while i < len1 and j < len2:
            a.append(word1[i])
            a.append(word2[j])
            i+=1
            j+=1
        
        while i < len1:
            a.append(word1[i])
            i+=1

        while j < len2:
            a.append(word2[j])
            j+=1

        return "".join(a)
        
