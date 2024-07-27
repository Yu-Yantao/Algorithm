class Solution:
    """
    424. 替换后的最长重复字符
    给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
    在执行上述操作后，返回 包含相同字母的最长子字符串的长度。

    示例 1：
    输入：s = "ABAB", k = 2
    输出：4

    示例 2：
    输入：s = "AABABBA", k = 1
    输出：4
    """

    def characterReplacement(self, s: str, k: int) -> int:
        """
        思路: 用一个counts，统计当前窗口内，出现次数最多的元素。
        当 窗口的大小 > 当前窗口内出现次数最多的元素的次数 + k 时，就要缩小窗口
        当缩小到 窗口的大小 = 当前窗口内出现次数最多的元素的次数 + k 时，意味着当前可以替换k次后，成为一个合法的子串
        :param s:
        :param k:
        :return:
        """
        max_count = 0
        ans = 0
        left, right = 0, 0
        counts = [0] * 26
        while right < len(s):
            counts[ord(s[right]) - ord('A')] += 1
            max_count = max(max_count, counts[ord(s[right]) - ord('A')])
            right += 1
            if right - left > max_count + k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            ans = max(ans, right - left)
        return ans


if __name__ == '__main__':
    print(Solution().characterReplacement('ABAB', 2))
