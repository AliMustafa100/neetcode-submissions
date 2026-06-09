class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #declare a hashmap
        #if num is in that hashmap we will increment the count
        #if it isnt then we will will add it to the list 
        #return the highest so we can do a max value


        hm = {}

        for num in nums:
            if num in hm:
                hm[num]+=1
            else:
                hm[num]=1
        
        return sorted(hm,key=hm.get,reverse=True)[:k]
