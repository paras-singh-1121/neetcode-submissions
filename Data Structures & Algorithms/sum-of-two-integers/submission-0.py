class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitShortner = 0xffffffff

        while (b & bitShortner) > 0:
            carry = (a & b) << 1
            a = (a ^ b) 
            b = carry
        return (a & bitShortner) if b > 0 else a