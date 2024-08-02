from typing import List


class Solution:
    """
    739. 每日温度
    给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

    示例 1:
    输入: temperatures = [73,74,75,71,69,72,76,73]
    输出: [1,1,4,2,1,1,0,0]

    示例 2:
    输入: temperatures = [30,40,50,60]
    输出: [1,1,1,0]
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        思路1: 从右向左遍历，维护一个单调递减的栈(存储元素的下标)，栈中的元素，作为最大值的候选项。以[73, 74, 75, 71, 69, 72, 76, 73]为例。  </br>

        1.73入栈，ans[7] = 0，stack = [7]
        2.76大于73，73出栈，栈为空，ans[6] = 0，76入栈，stack = [6]
        3.72小于76，栈非空，ans[5] = 1(栈顶元素 - 当前元素的下标，6 - 5)，72入栈，stack = [6, 5]
        4.69小于72，栈非空，ans[4] = 1(栈顶元素 - 当前元素的下标，5 - 4)，69入栈，stack = [6, 5, 4]
        5.71大于69，69就要出栈，栈顶元素变为72，栈非空，ans[3] = 2(栈顶元素 - 当前元素的下标，5 - 3)，71入栈，stack[6, 5, 3]
        以此类推
        :param temperatures:
        :return:
        """
        if len(temperatures) == 1:
            return [0]
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            t = temperatures[i]
            while stack and t >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans

    def dailyTemperaturesLR(self, temperatures: List[int]) -> List[int]:
        """
        从左向右的解法，栈中保存的是还未找到下一个大于自身的元素，所以也是需要维护一个单调递减的栈，当新元素大于栈顶时，逐个出栈
        :param temperatures:
        :return:
        """
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            t = temperatures[i]
            while stack and t > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans


if __name__ == '__main__':
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
