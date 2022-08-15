# Given two strings S1 and S2 as input, the task is 
# to merge them alternatively i.e. the first character of S1 then the first character of S2 and so on till the strings end.
# NOTE: Add the whole string if other string is empty

class Solution:
    def merge(self, S1, S2):
        # code here
        _min = min(len(S1),len(S2))
        extra = S1[_min::]+S2[_min::]
        out = ""
        for i in range(_min):
            out += S1[i]+S2[i]
        return(out+extra)