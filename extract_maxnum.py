class Solution:
    def extractMaximum(self,S):
        import re
        # code here
        digits = re.findall(r'\d+',S)
        digits = [int(i) for i in digits]
        if digits == []:
            return -1
        return max(digits)