# Given a string S, check if it is palindrome or not.

class Solution:
	def isPalindrome(self, S):
		# code here
		if S == S[::-1]:
		    return 1
		return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    S = "seles"
    ob = Solution()
    answer = ob.isPalindrome(S)
    print(answer)

# } Driver Code Ends