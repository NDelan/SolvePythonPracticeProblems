# Given two stringsaandbconsisting of lowercase characters. 
# The task is to check whether two given strings are an anagram of each other or not. 
# An anagram of a string is another string that contains the same characters, only the order of characters can be different. 
# For example, act and tac are an anagram of each other.

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        x = list(a)
        x.sort()
        y = list(b)
        y.sort()
        if x == y:
            return True
        else:
            return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends