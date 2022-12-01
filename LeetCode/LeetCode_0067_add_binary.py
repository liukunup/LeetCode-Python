#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-01 11:25:35

# 导入所需的依赖库
import unittest

# 题目编号: 67
# 题目名称: 二进制求和
# 题目难度: Easy

# 知识点: 位运算, 数学, 字符串, 模拟

# 题目详情:
"""
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。

&nbsp;

示例&nbsp;1：


输入:a = "11", b = "1"
输出："100"

示例&nbsp;2：


输入：a = "1010", b = "1011"
输出："10101"

&nbsp;

提示：


	1 &lt;= a.length, b.length &lt;= 104
	a 和 b 仅由字符 '0' 或 '1' 组成
	字符串如果不是 "0" ，就不含前导零


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            ans = x ^ y
            carry = (x & y) << 1
            x, y = ans, carry
        return bin(x)[2:]


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual(self.inst.addBinary(a="11", b="1"), "100")
        self.assertEqual(self.inst.addBinary(a="1010", b="1011"), "10101")


if __name__ == "__main__":
    unittest.main()
