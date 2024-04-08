class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = len(students)
        count = {}

        for s in students:
            if s not in count:
                count[s] = 0
            count[s] += 1

        for s in sandwiches:
            if s not in count or count[s] <= 0:
                return result
            elif count[s] > 0:
                result -= 1
                count[s] -= 1
        return result

#Time: O(n)
#Space: O(n)