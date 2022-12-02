#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-02 17:44:54

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 22
# 题目名称: 括号生成
# 题目难度: Medium

# 知识点: 字符串, 动态规划, 回溯

# 题目详情:
"""
数字 n&nbsp;代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

&nbsp;

示例 1：


输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]


示例 2：


输入：n = 1
输出：["()"]


&nbsp;

提示：


	1 &lt;= n &lt;= 8


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans

# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(0, -1)


if __name__ == "__main__":
    unittest.main()
