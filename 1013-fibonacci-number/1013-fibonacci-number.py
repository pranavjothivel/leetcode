class Solution:
    # def fib(self, n: int, memo={}) -> int:
    #     if n == 0:
    #         return 0
    #     elif n == 1:
    #         return 1

    #     if n not in memo:
    #         memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)
    #     return memo[n]
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        memo = [0, 0, 1]

        for i in range(2, n + 1):
            memo[0] = memo[1]
            memo[1] = memo[2]
            memo[2] = memo[0] + memo[1]

        return memo[2]