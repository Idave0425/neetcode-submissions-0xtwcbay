class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups hashkap that stores key and group of anagrams for that key
        # find key for each word in string
        # groups[key].append string
        # return a list of the values of group

        groups = {}

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            
            key = tuple(count)

            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        
        return list(groups.values())

        
