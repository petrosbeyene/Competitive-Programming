class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        
        cnt_dict = Counter(deck)
        cnt_arr = list(cnt_dict.values())

        if len(cnt_arr) == 1 and cnt_arr[0] > 1:
            return True

        ans_gcd = gcd(cnt_arr[0], cnt_arr[1])
        for i in range(2, len(cnt_arr)):
            ans_gcd = gcd(ans_gcd, cnt_arr[i])
        
        return ans_gcd > 1
