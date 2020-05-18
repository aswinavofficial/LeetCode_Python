# This is an exclusive problem only available in the Complete and Deluxe versions of this course.
# To learn more, visit https://kaeducation.com/lc-py.html


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        d = {}
        l = []
        j = 0

        for i in strs:
            k = "".join(sorted(i))

            if k in d.keys():
                d[k].append(i)
            else:
                d[k] = [i]
        return d.values()
