#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-30 20:02:39

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 17
# 题目名称: 电话号码的字母组合
# 题目难度: Medium

# 知识点: 哈希表, 字符串, 回溯

# 题目详情:
"""
给定一个仅包含数字&nbsp;2-9&nbsp;的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



&nbsp;

示例 1：


输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]


示例 2：


输入：digits = ""
输出：[]


示例 3：


输入：digits = "2"
输出：["a","b","c"]


&nbsp;

提示：


	0 &lt;= digits.length &lt;= 4
	digits[i] 是范围 ['2', '9'] 的一个数字。


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(conbination, nextdigit):
            if len(nextdigit) == 0:
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    backtrack(conbination + letter, nextdigit[1:])

        res = []
        backtrack('', digits)
        return res


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
