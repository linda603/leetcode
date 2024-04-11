class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        count = 0

        while l <= r:
            count += 1
            remainWeight = limit - people[r]
            
            if people[l] <= remainWeight:
                l += 1
            r -= 1
        
        return count

#Time: O(nlogn)
#Space: O(logn)
