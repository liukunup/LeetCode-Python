#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-27 13:34:53

# 导入所需的依赖库
import unittest

# 题目编号: 20
# 题目名称: 有效的括号
# 题目难度: Easy

# 知识点: 栈, 字符串

# 题目详情:
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']'&nbsp;的字符串 s ，判断字符串是否有效。

有效字符串需满足：


	左括号必须用相同类型的右括号闭合。
	左括号必须以正确的顺序闭合。
	每个右括号都有一个对应的相同类型的左括号。


&nbsp;

示例 1：


输入：s = "()"
输出：true


示例&nbsp;2：


输入：s = "()[]{}"
输出：true


示例&nbsp;3：


输入：s = "(]"
输出：false


&nbsp;

提示：


	1 &lt;= s.length &lt;= 104
	s 仅由括号 '()[]{}' 组成


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def isValid(self, s: str) -> bool:
        dic = {
            "{": "}",
            "[": "]",
            "(": ")",
            "?": "?"
        }
        stack = ["?"]
        for ch in s:
            if ch in dic:
                stack.append(ch)
            elif dic[stack.pop()] != ch:
                return False
        return len(stack) == 1


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
