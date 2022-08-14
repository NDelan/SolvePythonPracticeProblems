# Given a string S, Check if characters of the given string 
# can be rearranged to form a palindrome.
# Note: You have to return 1 if it is possible to convert 
# the given string into palindrome else return 0. 
class Solution:

    def isPossible(self, S):

        # code here
        _dict = {}
        for i in S:
            _dict.setdefault(i,0)
            _dict[i]+=1
        _list = [val for val in _dict.values()]
        odd = 0
        for i in _list:
            if i%2 != 0:
                odd +=1
        if odd > 1:
            return 0
        else:
            return 1