import math
import bisect
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions_sorted = sorted(potions)
        res = []
        n = len(potions_sorted)

        for spell in spells:
            minimum_potion = math.ceil(success/spell)
            minimum_potion_idx = bisect.bisect_left(potions_sorted, minimum_potion)
            res.append(n - minimum_potion_idx)

        return res
                