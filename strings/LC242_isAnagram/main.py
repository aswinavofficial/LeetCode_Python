# This is an exclusive problem only available in the Complete and Deluxe versions of this course.
# To learn more, visit https://kaeducation.com/lc-py.html


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False
