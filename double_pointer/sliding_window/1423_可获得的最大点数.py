from typing import List


class Solution:
    """
    1423. 可获得的最大点数
    几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。
    每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。
    你的点数就是你拿到手中的所有卡牌的点数之和。
    给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。

    示例 1：
    输入：cardPoints = [1,2,3,4,5,6,1], k = 3
    输出：12
    解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。
    """
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        思路：题目要求只能从左右两边取出和最大的 k 张牌，那么剩下的 n - k 张牌，一定是一个连续的子数组。n - k 的子数组的和最小时，那取出的 k 张牌一定是最大的。
        所以只需要转换思路，求出一个连续子数组的和最小值，即可求出最大点数。
        :param cardPoints:
        :param k:
        :return:
        """
        m = len(cardPoints) - k
        min_sum = window = sum(cardPoints[:m])
        for i in range(m, len(cardPoints)):
            window = window + cardPoints[i] - cardPoints[i - m]
            min_sum = min(min_sum, window)
        return sum(cardPoints) - min_sum


if __name__ == '__main__':
    print(Solution().maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3))
    print(Solution().maxScore(cardPoints=[96, 90, 41, 82, 39, 74, 64, 50, 30], k=8))
