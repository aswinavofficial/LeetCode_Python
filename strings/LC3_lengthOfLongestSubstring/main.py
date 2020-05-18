class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = s
        # Creating a set to store the last positions of occurrence
        seen = {}
        maximum_length = 0

        # starting the inital point of window to index 0
        start = 0

        for end in range(len(string)):
            # Checking if we have already seen the element or not
            if string[end] in seen:
                start = max(start, seen[string[end]] + 1)
            seen[string[end]] = end
            maximum_length = max(maximum_length, end - start + 1)
        return maximum_length
