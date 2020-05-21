class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 3:
            return n

        w = [0, 1, 2, 3]
        i = 4
        while i <= n:
            print("wi-2", w[i - 2])
            w.append(w[i - 1] + w[i - 2])
            i = i + 1
        return w[n]
