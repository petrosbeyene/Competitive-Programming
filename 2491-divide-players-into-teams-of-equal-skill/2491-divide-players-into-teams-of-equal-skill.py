class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total_skill = sum(skill)

        n = len(skill)
        if n == 2:
            return skill[0]*skill[1]

        skill_per_team = total_skill/(n/2)
        if not skill_per_team.is_integer():
            return -1
        
        ans = 0
        i, j = 0, len(skill)-1
        while i < j:
            if skill[i] + skill[j] != skill_per_team:
                return -1
            ans += (skill[i]*skill[j])
            i += 1
            j -= 1
        
        return ans
        
