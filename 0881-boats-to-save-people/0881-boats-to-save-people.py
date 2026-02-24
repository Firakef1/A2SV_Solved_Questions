class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        counter = 0
        left, right = 0, len(people)-1

        while left <= right:
            if people[left]+people[right] <= limit:
                counter += 1
                left += 1
                right -= 1
            else:
                counter += 1
                right -= 1

        return counter
