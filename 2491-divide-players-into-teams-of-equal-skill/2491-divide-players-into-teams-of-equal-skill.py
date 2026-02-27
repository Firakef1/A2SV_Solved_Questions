class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        left = 0
        right = len(skill)-1

        skill_sum = skill[left] + skill[right]
        total = 0

        while left < right:

            if skill[left] + skill[right] == skill_sum:
                total += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1
        
        return total