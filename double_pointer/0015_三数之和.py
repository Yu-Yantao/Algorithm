from typing import List


class Solution:
    """
    15. 三数之和
    给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
    你返回所有和为 0 且不重复的三元组。
    注意：答案中不可以包含重复的三元组。

    示例 1：
    输入：nums = [-1,0,1,2,-1,-4]
    输出：[[-1,-1,2],[-1,0,1]]
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        思路：对数组进行排序，遍历数组，固定一个值，双指针枚举另外两个值。
        :param nums:
        :return:
        """
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            # 三数之和为0，最小值必为负数，如果nums[k]大于0，一定无法组成一个答案
            if nums[k] > 0:
                break
            # 跳过重复项
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            # 双指针
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    # 跳过重复项
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    # 跳过重复项
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res
