class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0]+digits

        rem = 1
        for i in range(len(digits)-1,-1,-1):
            curr = digits[i]+rem
            digits[i] = curr%10
            rem = curr//10

        if digits[0] == 0:
            return digits[1:]
        return digits