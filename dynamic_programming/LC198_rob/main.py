class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        m = max(nums[0], nums[1])
        dp = [nums[0], m]

        for i in range(2, len(nums)):
            p = dp[i - 2] + nums[i]
            m = max(p, dp[i - 1])
            dp.append(m)
        return dp.pop()
