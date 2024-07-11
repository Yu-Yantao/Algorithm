class Solution:
    """
    125. 验证回文串
    如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
    字母和数字都属于字母数字字符。
    给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。

    示例 1：
    输入: s = "A man, a plan, a canal: Panama"
    输出：true
    解释："amanaplanacanalpanama" 是回文串。
    """
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def check(c):
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9':
                return True
            return False

        while l < r:
            #
            while l < r and not check(s[l]):
                l += 1
            while l < r and not check(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
