class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


       hm = {}

       for words in strs:
        key = ''.join(sorted(words))

        if key in hm:
            hm[key].append(words)
        else:
            hm[key] = [words]

       return list(hm.values())


