#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-21 22:45:18

# 导入所需的依赖库
import unittest

# 题目编号: 5
# 题目名称: 最长回文子串
# 题目难度: Medium

# 知识点: 字符串, 动态规划

# 题目详情:
"""
给你一个字符串 s，找到 s 中最长的回文子串。

&nbsp;

示例 1：


输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。


示例 2：


输入：s = "cbbd"
输出："bb"


&nbsp;

提示：


	1 &lt;= s.length &lt;= 1000
	s 仅由数字和英文字母组成


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def longestPalindrome(self, s: str) -> str:
        # 长度小于2
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0

        # dp[i][j] 表示 s[i..j] 是否为回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for sub_s_len in range(2, n + 1):
            for i in range(n):
                j = sub_s_len + i - 1
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        return s[begin:begin + max_len]


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual(self.inst.longestPalindrome("babad"), "bab")

    def test_2(self):
        self.assertEqual(self.inst.longestPalindrome("cbbd"), "bb")


if __name__ == "__main__":
    unittest.main()
