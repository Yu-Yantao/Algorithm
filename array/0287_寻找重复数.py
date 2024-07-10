from typing import List


class Solution:
    """
    287. 寻找重复数
    给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
    假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
    你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

    示例 1：
    输入：nums = [1,3,4,2,2]
    输出：2
    """
    def findDuplicate(self, nums: List[int]) -> int:
        """
        思路：这里介绍二分的思路，哈希表和快慢指针不做介绍
        由题可知，必有重复数，重复数在 [1,n] 之间，用例也做了限制，仅有一个重复数
        对于任意一个数 x ，在无重复数的数组中，小于等于 x 的数，应该是 x 个，分析如下：
            把数组二分[1,x]和[x + 1,n]，左区间的数字个数是x。
        那么如果小于等于x的数个数大于x，那么重复数在[1,x]中，否则在[x + 1,n]中。

        这道题使用二分法的难点在于不是在原始数组中进行二分，而是对[1,n]这个区间内的数进行二分，数组仅做辅助计算。
        :param nums:
        :return:
        """
        left, right = 1, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    print(Solution().findDuplicate([1, 3, 4, 2, 2]))
