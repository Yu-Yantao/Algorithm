from typing import List


class Solution:
    """
    713. 乘积小于 K 的子数组
    给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。

    示例 1：
    输入：nums = [10,5,2,6], k = 100
    输出：8

    示例 2：
    输入：nums = [1,2,3], k = 0
    输出：0
    """
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        思路: 维护一个窗口，不断增大右指针，当乘积大于k时，缩小左指针，同时记录窗口内的子数组个数
        这里有一个技巧: 在向右移动的过程中，每向窗口中增加一个数num时(假设加上num后，数组的乘积小于k)，那么以num结尾的子数组，是right - left + 1。
        实际上，我们也主需要关注以num结尾的子数组，因为在之前的遍历中，其他数组都已经被处理过了。
        :param nums:
        :param k:
        :return:
        """
        if k <= 1:
            return 0
        count = 1
        left, right = 0, 0
        ans = 0
        while right < len(nums):
            count *= nums[right]
            while count >= k:
                count /= nums[left]
                left += 1
            ans += (right - left + 1)
            right += 1
        return ans
