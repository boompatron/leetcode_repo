class Solution:
    def reverse(self, x: int) -> int:
        is_positive = True
        # if x < -pow(2, 31) or x >= pow(2, 31):
        #     return 0
        if x < 0:
            x = -x
            is_positive = False
        ans = 0
        while x:
            ans *= 10
            ans += (x % 10)
            x //= 10
        if ans < -pow(2, 31) or ans >= pow(2, 31):
            return 0
        return ans if is_positive else -ans
