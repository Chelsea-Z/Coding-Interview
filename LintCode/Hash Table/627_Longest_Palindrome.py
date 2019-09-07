class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        leng = 0
        chars = {}
        for c in s:
            if c in chars.keys():
                del chars[c]
                leng += 2
            else:
                chars[c] = 1
            
        if len(chars.keys())>0:
            leng += 1 
        
        return leng 