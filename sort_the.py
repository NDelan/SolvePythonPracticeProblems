# Given a string str containing only lower case alphabets, 
# the task is to sort it in lexicographically-descending order.
# Input: str = "geeks"
# Output: "skgee"
# Explanation: It's the lexicographically-
# descending order.
class Solution:
    def ReverseSort(self, str): 
        # code here
        x = list(str)
        x.sort()
        nstr = ""
        for i in x:
            nstr+=i
        return nstr[::-1]