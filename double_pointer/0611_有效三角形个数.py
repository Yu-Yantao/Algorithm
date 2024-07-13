from typing import List


class Solution:
    """
    611. 有效三角形的个数
    给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。

    示例 1:
    输入: nums = [2,2,3,4]
    输出: 3
    解释:有效的组合是:
    2,3,4 (使用第一个 2)
    2,3,4 (使用第二个 2)
    2,2,3
    """
    def triangleNumber(self, nums: List[int]) -> int:
        """
        思路：先进行排序，从第三项开始遍历数组，第i项做为第三条边，从[0,i-1]内依次枚举，作为另外两条边
        优化思路：
        当nums[left] + nums[right] <= nums[i]时（两边只和小于等于第三边），则无法构成三角形，将left + 1。
        当nums[left] + nums[right] > nums[i]时（两边和大于等于第三边），则存在三角形。
        此时需要更新ans，更新规则如下：
            此时num[left] <= [right] <= nums[i]，并且nums[left] + nums[right] > nums[i]，那么从[left, right)区间内任取一点x
            必有第三边大于等于nums[x] + nums[right] > nums[i]的，所以更新ans += (right - left)
        :param nums:
        :return:
        """
        nums.sort()
        size = len(nums)
        ans = 0

        for i in range(2, size):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] <= nums[i]:
                    left += 1
                else:
                    ans += (right - left)
                    right -= 1
        return ans


if __name__ == '__main__':
    print(Solution().triangleNumber([2, 2, 3, 4]))
