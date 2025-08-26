#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2025-08-26 22:22:10

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 125
# 题目名称: 验证回文串
# 题目难度: Easy

# 知识点: 双指针, 字符串

# 题目详情:
"""
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。

&nbsp;

示例 1：


输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。


示例 2：


输入：s = "race a car"
输出：false
解释："raceacar" 不是回文串。


示例 3：


输入：s = " "
输出：true
解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。


&nbsp;

提示：


	1 &lt;= s.length &lt;= 2 * 105
	s 仅由可打印的 ASCII 字符组成


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]

# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(self.inst.isPalindrome(s = "A man, a plan, a canal: Panama"), True)


if __name__ == "__main__":
    unittest.main()
