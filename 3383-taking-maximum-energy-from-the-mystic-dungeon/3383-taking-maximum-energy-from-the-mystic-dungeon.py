class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = energy.copy()
        for i in range(len(dp) - k - 1, -1, -1):
            dp[i] = dp[i + k] + energy[i]
        return max(dp)