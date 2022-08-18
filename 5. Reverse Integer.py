class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        if str(x)[0]=="-":
            y = int(str(x)[::-1][:-1]) * -1
        else:
            y = int(str(x)[::-1])
        if -2**31 <= y <= 2**31 - 1:
            return y
        return 0