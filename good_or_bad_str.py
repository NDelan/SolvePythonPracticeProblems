# In this problem, a String S is composed of lowercase alphabets and 
# wildcard characters i.e. '?'. Here, '?' can be replaced by any of the lowercase 
# alphabets. Now you have to classify the given String on the basis of following rules:
# If there are more than 3 consonants together or more than 5 vowels together, the
#  String is considered to be "BAD". A String is considered "GOOD" only if it is not “BAD”.
# NOTE: String is considered as "BAD" if the above condition is satisfied even once. Else it is "GOOD" and the task is to make the string "BAD".
class Solution:
    def isGoodorBad(self, S):
        # code here
        vowels = ['a','e','i','o','u']
        vow_cnt = 0
        cons_cnt = 0
        for i in S:
            if i in vowels:
                vow_cnt+=1
                cons_cnt = 0
            elif i == '?':
                vow_cnt+=1
                cons_cnt+=1
            else:
                cons_cnt += 1
                vow_cnt = 0
            if cons_cnt > 3 or vow_cnt > 5:
                return 0
        return 1 