# This is an exclusive problem only available in the Deluxe version of this course.
# To learn more, visit https://kaeducation.com/lc-py.html


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        for i in S:
            if i != "#":
                stack1.append(i)
            elif len(stack1) > 0:
                stack1.pop()

        for i in T:
            if i != "#":
                stack2.append(i)
            elif len(stack2) > 0:
                stack2.pop()
        if len(stack1) != len(stack2):
            return False

        for i in range(len(stack1)):
            if stack1[i] != stack2[i]:
                return False
        return True

