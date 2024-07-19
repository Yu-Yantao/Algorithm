class Solution:
    """
    3. 无重复字符的最长子串
    给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串的长度。

    示例 1:
    输入: s = "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

    示例 2:
    输入: s = "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        思路: 滑动窗口
        通过两个指针控制窗口的大小，当窗口内没有重复字符时，记录窗口大小，当窗口内有重复字符时，窗口左边界向右移动，直到窗口内没有重复字符
        :param s:
        :return:
        """
        if len(s) < 2:
            return len(s)
        left, right = 0, 0
        res = 0
        while right < len(s):
            if s[right] in s[left:right]:
                left += 1
            else:
                right += 1
                res = max(res, right - left)
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
