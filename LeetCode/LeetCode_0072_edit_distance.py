#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-22 00:22:58

# 导入所需的依赖库
import unittest

# 题目编号: 72
# 题目名称: 编辑距离
# 题目难度: Hard

# 知识点: 字符串, 动态规划

# 题目详情:
"""
给你两个单词&nbsp;word1 和&nbsp;word2， 请返回将&nbsp;word1&nbsp;转换成&nbsp;word2 所使用的最少操作数 &nbsp;。

你可以对一个单词进行如下三种操作：


	插入一个字符
	删除一个字符
	替换一个字符


&nbsp;

示例&nbsp;1：


输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -&gt; rorse (将 'h' 替换为 'r')
rorse -&gt; rose (删除 'r')
rose -&gt; ros (删除 'e')


示例&nbsp;2：


输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -&gt; inention (删除 't')
inention -&gt; enention (将 'i' 替换为 'e')
enention -&gt; exention (将 'n' 替换为 'x')
exention -&gt; exection (将 'n' 替换为 'c')
exection -&gt; execution (插入 'u')


&nbsp;

提示：


	0 &lt;= word1.length, word2.length &lt;= 500
	word1 和 word2 由小写英文字母组成


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        """ word1(src) -> word2(dst) """
        # 两个字符串的长度
        m = len(word1)
        n = len(word2)
        # 判断是否有空串
        if n * m == 0:
            return n + m
        #
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        #
        for i in range(n + 1):
            dp[0][i] = i
        for j in range(m + 1):
            dp[j][0] = j
        #
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                left = dp[j][i - 1] + 1
                down = dp[j - 1][i] + 1
                left_down = dp[j - 1][i - 1]
                if word1[j - 1] != word2[i - 1]:
                    left_down += 1
                dp[j][i] = min(left, down, left_down)
        return dp[m][n]


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual(self.inst.minDistance("horse", "ros"), 3)

    def test_2(self):
        self.assertEqual(self.inst.minDistance("intention", "execution"), 5)


if __name__ == "__main__":
    unittest.main()
