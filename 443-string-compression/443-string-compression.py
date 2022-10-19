class Solution:
    def compress(self, chars) -> int:
        first = 0
        second = 1
        temp = []
        
        if len(chars) == 0 or len(chars) == 1:
            return len(chars)
        
        while second < len(chars):
            if chars[first]!=chars[second]:
                temp.append(chars[first])
                if second == len(chars)-1:
                    temp.append(chars[second])
                first += 1
                second += 1
            else:
                while second < len(chars) and chars[first]==chars[second]:
                    second += 1
                grp_len = second - first
                
                if grp_len == 1:
                    temp.append(chars[first])
                else:
                    temp.extend([chars[first]] + list(str(grp_len)))
                first = second
        
        chars[:] = temp
        return len(chars)