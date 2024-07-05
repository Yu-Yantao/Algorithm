class Solution:
    """
    154. 寻找旋转排序数组中的最小值 II
    已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
    若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
    若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]

    给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

    示例 1：
    输入：nums = [1,3,5]
    输出：1
    """

    def findMin(self, nums: [int]) -> int:
        """
        思路：使用二分查找，逐步缩小范围
        :param nums:
        :return:
        """
        left, right = 0, len(nums) - 1
        while left < right:
            """
            这里的比较，都是使用num[mid]和nums[right]比较，原因如下
            对于一个旋转后的数组，数组会被分为两个有序数组，如下两种情况
            [1, 2, 3, 4, 5]
            [3, 4, 5, 1, 2]
            left = 0, right = 4, mid = 2
            两个数组中均满足，nums[mid] > nums[left]，但最小值却不在m的同侧

            """
            mid = (left + right) // 2
            # mid大于right，最小值在右边，并且最小值一定不是mid，更新右边界为mid+1
            if nums[mid] > nums[right]:
                left = mid + 1
            # mid小于right，最小值在左边，并且有可能是mid，更新右边界为mid
            elif nums[mid] < nums[right]:
                right = mid
            # mid等于right，缩小右边界
            else:
                """
                1.为什么缩小右边界？
                因为比较是基于right进行比较的
                2.减一会不会遗漏元素？
                分两种情况讨论
                i.最小值在右边
                [3, 3, 3, 3a, 1, 2, 3b]
                此时3a = 3b，如果3是最小值，那么从3a到3b，即使去掉3b，也还有3a以及3a到3b中间的3
                如果3不是最小值，那么3b可以安全的去掉
                ii.最小值在左边
                分析方式同上，
                [3, 1, 3, 3, 3]
                对于这种情况
                """
                right -= 1
        return nums[left]


if __name__ == '__main__':
    print(Solution().findMin([3, 1, 3]))
    print(Solution().findMin([3, 3, 3, 1, 3]))
    print(Solution().findMin([5, 6, 1, 2, 3, 4]))
