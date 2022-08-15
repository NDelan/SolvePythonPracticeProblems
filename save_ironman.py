# Jarvis is weak in computing palindromes for Alphanumeric characters.
# While Ironman is busy fighting Thanos, he needs to activate sonic 
# punch but Jarvis is stuck in computing palindromes.
# You are given a string S containing alphanumeric characters. 
# Find out whether the string is a palindrome or not.
# If you are unable to solve it then it may result in the death of Iron Man.
def saveIronman (s) : 
    #Complete the function
    s = s.lower()
    y = ""
    for i in s:
        if i.isalnum():
            y+=i
    if y == y[::-1]:
        return True
    return False