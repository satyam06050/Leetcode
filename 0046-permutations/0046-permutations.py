class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def b(path):
            if len(path)==len(nums):
                result.append(path[:])
            for i in nums:
                if i not in path:
                    path.append(i)
                    b(path)
                    path.pop()
        b([])
        return result                
        
        