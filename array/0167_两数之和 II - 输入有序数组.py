from typing import List


class Solution:
    """
    167. 两数之和 II - 输入有序数组
    给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

    示例 1：
    输入：numbers = [2,7,11,15], target = 9
    输出：[1,2]
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        思路：利用双指针，从两边向中间找，numbers[l] + numbers[r] 大于 target，则 r--；小于 target，则 l++
        :param numbers:
        :param target:
        :return:
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1
        return [-1, -1]


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
