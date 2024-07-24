from typing import List


class Solution:
    """
    674. 最长连续递增序列
    给定一个未经排序的整数数组，找到最长且 连续递增 的子序列，并返回该序列的长度。

    示例 1：
    输入：nums = [1,3,5,4,7]
    输出：3
    """

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        left, right = 0, 1
        max_length = 1
        while right < len(nums):
            if nums[right] > nums[right - 1]:
                right += 1
            else:
                max_length = max(max_length, right - left)
                left = right
                right += 1
        # 对于严格递增的子序列，不会进上述else分支，最后需要单独处理
        return max(max_length, right - left)


if __name__ == '__main__':
    # print(Solution().findLengthOfLCIS([1, 3, 5, 4, 7]))
    print(Solution().findLengthOfLCIS([1, 3, 5, 7]))
    # print(Solution().findLengthOfLCIS([2, 2, 2, 2, 2]))
