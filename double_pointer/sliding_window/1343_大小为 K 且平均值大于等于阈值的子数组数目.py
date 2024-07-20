from typing import List


class Solution:
    """
    1343. 大小为 K 且平均值大于等于阈值的子数组数目
    给你一个整数数组 arr 和两个整数 k 和 threshold 。
    请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。

    示例 1：
    输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
    输出：3
    解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。
    """
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        left, right = 0, 0
        count = 0
        ans = 0
        while right < n:
            count += arr[right]
            right += 1
            # 使用乘法，优化平均值的比较，题目给出的范围小，不会溢出
            while count >= threshold * k and right - left >= k:
                if right - left == k:
                    ans += 1
                count -= arr[left]
                left += 1

        return ans


if __name__ == '__main__':
    print(Solution().numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))
    print(Solution().numOfSubarrays(arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5))
