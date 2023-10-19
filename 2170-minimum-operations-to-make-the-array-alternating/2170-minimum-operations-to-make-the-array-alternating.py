class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 1:
            return 0

        even_idx_elems = {}
        odd_idx_elems = {}
        for i in range(n):
            if i % 2 == 0:
                even_idx_elems[nums[i]] = even_idx_elems.get(nums[i], 0) + 1
            else:
                odd_idx_elems[nums[i]] = odd_idx_elems.get(nums[i], 0) + 1
                

        evens = sorted((val, key) for key, val in even_idx_elems.items())
        odds = sorted((val, key) for key, val in odd_idx_elems.items())

        if evens[-1][1] != odds[-1][1]:
            return n - (evens[-1][0] + odds[-1][0])
        
        # in case the most frequent elems at both the 
        # even and odd indexes is the same I will have to choices
        # choice 1: to combine the max frequent elem of evens with scnd max frequent elem of odds
        # choice 2: to combine scnd max frequent elem of evens with the max frequent elem of odds

        choice1 = n - evens[-1][0] - (odds[-2][0] if len(odds) > 1 else 0)
        choice2 = n - odds[-1][0] - (evens[-2][0] if len(evens) > 1 else 0)

        return min(choice1, choice2)
