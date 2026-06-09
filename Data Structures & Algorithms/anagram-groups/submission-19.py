class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = {}
        
        for w in strs:
            key = ''.join(sorted(w))

            if key in hm:
                hm[key].append(w)
            else:
                hm[key]=[w]
        return list(hm.values())



