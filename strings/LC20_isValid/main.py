# This is an exclusive problem only available in the Deluxe version of this course.
# To learn more, visit https://kaeducation.com/lc-py.html

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        dictp = {"(":")","{":"}","[":"]"}
        for i in s:
            
            if i in dictp.keys():
                stack.append(i)
                
            elif  len(stack) == 0 or dictp[stack.pop()] != i:
                return False
            
        return len(stack) == 0
        
