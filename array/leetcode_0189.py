from typing import List


class Solution:
    """
    给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
    示例 1:
    输入: [1,2,3,4,5,6,7] 和 k = 3
    输出: [5,6,7,1,2,3,4]
    解释:
    向右旋转 1 步: [7,1,2,3,4,5,6]
    向右旋转 2 步: [6,7,1,2,3,4,5]
    向右旋转 3 步: [5,6,7,1,2,3,4]
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, end):
            """
            翻转数组的指定区间
            :param nums: 数组
            :param start: 起始位置
            :param end: 结束位置
            :return:
            """
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k = k % len(nums)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
        reverse(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate(nums, k)
    print(nums)
