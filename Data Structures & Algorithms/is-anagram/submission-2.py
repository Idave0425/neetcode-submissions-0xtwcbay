class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = {}
        hashMapT = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            # if it doesn't exist in the hashMap, default value is 0
            hashMapS[s[i]] = 1 + hashMapS.get(s[i], 0)
            hashMapT[t[i]] = 1 + hashMapT.get(t[i], 0)

        for char in hashMapS:
            # if the char doesn't exist in hashMapT, default value is 0
            if hashMapS[char] != hashMapT.get(char, 0):
                return False

        return True
            