class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        s=sorted(set(arr))
        rank={}
        for i,j in enumerate(s):
            rank[j]=i+1
        return [rank[num] for num in arr]    



            

        