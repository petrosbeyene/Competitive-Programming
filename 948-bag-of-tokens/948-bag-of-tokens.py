class Solution:
    def bagOfTokensScore(self, tokens, power: int) -> int:
        tokens.sort()
        beg, end = 0, len(tokens)-1
        max_score = score = 0
        while beg <= end:
            if power >= tokens[beg]:
                power -= tokens[beg]
                score += 1
                max_score= max(max_score, score)
                beg += 1
            elif score > 0:
                power += tokens[end]
                score -= 1
                end -= 1
            else:
                break
        return max_score