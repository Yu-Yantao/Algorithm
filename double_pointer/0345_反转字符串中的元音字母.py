class Solution:
    """
    给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
    元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。

    示例 1：
    输入：s = "hello"
    输出："holle"
    """

    def reverseVowels(self, s: str) -> str:
        def is_vowel(ch: str) -> bool:
            return ch in "aeiouAEIOU"

        n = len(s)
        s = list(s)
        i, j = 0, n - 1
        while i < j:
            while i < n and not is_vowel(s[i]):
                i += 1
            while j > 0 and not is_vowel(s[j]):
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)


if __name__ == '__main__':
    print(Solution().reverseVowels("hello"))
