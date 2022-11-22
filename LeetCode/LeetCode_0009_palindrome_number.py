#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-22 23:40:42

# 导入所需的依赖库
import unittest

# 题目编号: 9
# 题目名称: 回文数
# 题目难度: Easy

# 知识点: 数学

# 题目详情:
"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。


	例如，121 是回文，而 123 不是。


&nbsp;

示例 1：


输入：x = 121
输出：true


示例&nbsp;2：


输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。


示例 3：


输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。


&nbsp;

提示：


	-231&nbsp;&lt;= x &lt;= 231&nbsp;- 1


&nbsp;

进阶：你能不将整数转为字符串来解决这个问题吗？

"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_num = 0
        while x > reverted_num:
            reverted_num = reverted_num * 10 + x % 10
            x //= 10

        return x == reverted_num or x == reverted_num // 10


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertTrue(self.inst.isPalindrome(121))

    def test_2(self):
        self.assertFalse(self.inst.isPalindrome(-121))

    def test_3(self):
        self.assertFalse(self.inst.isPalindrome(10))

    def test_4(self):
        self.assertTrue(self.inst.isPalindrome(11))


if __name__ == "__main__":
    unittest.main()
