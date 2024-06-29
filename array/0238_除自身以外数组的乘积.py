from typing import List


class Solution:
    """
    238. 除自身以外数组的乘积
    给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

    示例 1:
    输入: nums = [1,2,3,4]
    输出: [24,12,8,6]
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        构造一个n*n的二维数组，对角线上的值为1，其余位置用nums填充
        那么第i行的乘积，就是除nums[i]之外各元素的乘积
        以[2, 3, 4, 5]为例
        1 3 4 5
        2 1 4 5
        2 3 1 5
        2 3 4 1
        在次基础上，有两种方法计算。
        方法1:构造真实的二维数组，遍历每行，求出乘积，时间复杂度为O(n^2)，每行的乘积都是O(n)，所以时间复杂度为O(n^2)
        方法2:使用一维数组，计算二维数组的乘积。
        具体如下：
        1.先 从上到下 计算下三角的值，ans = [1, 2, 6, 24]
        2.然后计算上三角，计算时要 从下往上 计算，分析如下
          从下往上计算时，可以使用一个临时变量来保存之前行的结果，再乘以当前nums[i]即可，节省空间
        :param nums:
        :return:
        """
        ans, tmp = [1] * len(nums), 1
        # 计算下三角的值（i位置的的值等于i-1位置的值乘以nums[i-1]）
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        # 计算上三角
        for i in range(len(nums) - 2, -1, -1):
            tmp *= nums[i + 1]
            ans[i] *= tmp
        return ans


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))
