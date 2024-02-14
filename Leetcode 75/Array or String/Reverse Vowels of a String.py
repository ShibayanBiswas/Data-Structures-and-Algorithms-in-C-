'''

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0 
        j = len(s) - 1
        s = list(s)

        while i < j:
            if s[i] in "aeiouAEIOU" and s[j] in "aeiouAEIOU":
                s[i], s[j] = s[j], s[i]
                i = i + 1
                j = j - 1
            elif s[i] in "aeiouAEIOU":
                j = j - 1
            else:
                i = i + 1
                
        return "".join(s)