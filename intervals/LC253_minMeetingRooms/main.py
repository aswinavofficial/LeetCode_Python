# This is an exclusive problem only available in the Deluxe version of this course.
# To learn more, visit https://kaeducation.com/lc-py.html

# Given an array of meeting time intervals consisting of start and end
# times [[s1,e1], [s2,e2],...], find the minimum number of conference
# rooms required.

# Example1
#     Input: intervals = [(0,30),(5,10),(15,20)]
#     Output: 2
#     Explanation:
#     We need two meeting rooms
#     room1: (0,30)
#     room2: (5,10),(15,20)

# Example2
#     Input: intervals = [(2,7)]
#     Output: 1
#     Explanation:
#     Only need one meeting room


class Solution:
    def minMeetingRooms(self, intervals):
