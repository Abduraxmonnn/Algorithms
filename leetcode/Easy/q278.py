# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    a = bool


class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        while True:
            mid = (left + right) // 2
            if isBadVersion(mid):
                if mid == 1:
                    return mid
                else:
                    if isBadVersion(mid - 1):
                        right = mid
                    else:
                        return mid
            else:
                if isBadVersion(mid + 1):
                    return mid+1
                else:
                    left = mid


if __name__ == '__main__':
    n = 5
    bad = 4
    print(Solution().firstBadVersion(n, bad))


#
#
# https://leetcode.com/problems/first-bad-version/
