class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical = []
        
        prev = head
        curr = head.next
        pos = 1
        
        while curr.next:
            # local maximum OR local minimum
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                critical.append(pos)
            
            prev = curr
            curr = curr.next
            pos += 1
        
        if len(critical) < 2:
            return [-1, -1]
        
        # minimum distance between consecutive critical points
        min_dist = min(critical[i] - critical[i-1] 
                       for i in range(1, len(critical)))
        
        # maximum distance = first to last
        max_dist = critical[-1] - critical[0]
        
        return [min_dist, max_dist]