from typing import List


class Solution:
    """
    18. 四数之和
    给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
    请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

    示例 1：
    输入：nums = [1,0,-1,0,-2,2], target = 0
    输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        # 枚举第一个数
        for a in range(n - 3):
            x = nums[a]
            # 跳过重复数字
            if a and x == nums[a - 1]:
                continue
            # 取出x和最小的三个数，如果这四数之和大于target，那么后面的数字都无法满足要求，这里是break
            if x + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                break
            # 取出x和最大的三个数，如果这四数之和小于target，那么x一定无法满足要求，这里是continue
            if x + nums[-3] + nums[-2] + nums[-1] < target:
                continue
            # 跳过重复数字
            for b in range(a + 1, n - 2):  # 枚举第二个数
                y = nums[b]
                # 跳过重复数字
                if b > a + 1 and y == nums[b - 1]:
                    continue
                if x + y + nums[b + 1] + nums[b + 2] > target:
                    break
                if x + y + nums[-2] + nums[-1] < target:
                    continue
                # 双指针枚举第三个数和第四个数
                c = b + 1
                d = n - 1
                while c < d:
                    # 四数之和
                    s = x + y + nums[c] + nums[d]
                    if s > target:
                        d -= 1
                    elif s < target:
                        c += 1
                    else:
                        ans.append([x, y, nums[c], nums[d]])
                        c += 1
                        # 跳过重复数字
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        d -= 1
                        # 跳过重复数字
                        while d > c and nums[d] == nums[d + 1]:
                            d -= 1
        return ans


if __name__ == '__main__':
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
