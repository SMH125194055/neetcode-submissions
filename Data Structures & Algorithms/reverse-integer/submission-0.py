class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        n = abs(x)
        while (n > 0):
            # temp = n%10
            res *= 10
            res += (n%10)
            n = n//10
        if x < 0:
            res *= -1

        return res if (res > -2147483648  and res < 2147483647) else 0 