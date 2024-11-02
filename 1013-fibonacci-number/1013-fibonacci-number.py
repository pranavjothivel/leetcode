class Solution:
    def fib(self, n: int, memo={}) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        if n not in memo:
            memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)  # Recursive calls with memoization
        return memo[n]