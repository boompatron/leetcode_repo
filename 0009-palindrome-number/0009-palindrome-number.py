from collections import deque


class Solution:
    def isPalindrome(self, x: int) -> bool:
        is_negative = False
        dq = deque()
        if x < 0:
            is_negative = True
            x = -x
        while x:
            dq.appendleft(x % 10)
            x //= 10
        if is_negative:
            dq.appendleft('-')
        for i in range(len(dq) // 2):
            left, right = dq.popleft(), dq.pop()
            if left != right:
                return False
        return True
