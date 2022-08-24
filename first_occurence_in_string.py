# Your task is to implement the function strstr. 
# The function takes two strings as arguments (s,x) and  
# locates the occurrence of the string x in the strings. The function returns 
# and integer denoting the first occurrence of the string x in s (0 based indexing).

def strstr(s,x):
    #code here
    if x in s:
        for i in range(len(s)):
            check = s[i:i+len(x)]
            if check == x:
                return i
                break
    else:
        return -1