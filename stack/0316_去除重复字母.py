class Solution:
    """
    316. 去除重复字母
    给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

    示例 1：
    输入：s = "bcabc"
    输出："abc"

    示例 2：
    输入：s = "cbacdcbc"
    输出："acdb"
    """

    def removeDuplicateLetters(self, s: str) -> str:
        """
        思路: 单调递增的栈

        1.统计每个字符的个数
        2.当遍历到i位置时，如果s[i]未出现在栈中，比较s[i]和栈顶元素，如果s[i]小于栈顶元素，并且栈顶元素在后面还会出现，则将栈顶元素弹出（不满足字典序最小），然后将当前元素入栈
        3.如果当前元素在栈中，则将count减1即可
        :param s:
        :return:
        """
        count = [0] * 26
        for i in s:
            count[ord(i) - ord('a')] += 1
        stack = []
        for i in s:
            if i not in stack:
                while stack and stack[-1] > i and count[ord(stack[-1]) - ord('a')] > 0:
                    stack.pop()
                stack.append(i)
            count[ord(i) - ord('a')] -= 1
        return ''.join(stack)


if __name__ == '__main__':
    # print(Solution().removeDuplicateLetters('bcabc'))
    # print(Solution().removeDuplicateLetters('cbacdcbc'))
    # print(Solution().removeDuplicateLetters('cdadabcc'))
    print(Solution().removeDuplicateLetters('bbcaac'))
