
class Solution:
    def findOriginalArray(self, changed):
        arrSize = len(changed)
        changed.sort()
        if arrSize % 2 != 0:
            return []
        
        count = Counter(changed)
        original = []
        
        for num in changed:
            if num == 0 and count[num] >= 2:
                original.append(num)
                count[num] -= 2
            elif num > 0 and count[num] and count[num*2]:
                original.append(num)
                count[num] -=1
                count[num*2] -= 1
        return original if len(original) == arrSize // 2 else []

        
            
            
        