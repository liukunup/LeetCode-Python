#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-08 17:01:13

# 导入所需的依赖库
import unittest

# 题目编号: 29
# 题目名称: 两数相除
# 题目难度: Medium

# 知识点: 位运算, 数学

# 题目详情:
"""
给定两个整数，被除数&nbsp;dividend&nbsp;和除数&nbsp;divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数&nbsp;dividend&nbsp;除以除数&nbsp;divisor&nbsp;得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

&nbsp;

示例&nbsp;1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

示例&nbsp;2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2

&nbsp;

提示：


	被除数和除数均为 32 位有符号整数。
	除数不为&nbsp;0。
	假设我们的环境只能存储 32 位有符号整数，其数值范围是 [&minus;231,&nbsp; 231&nbsp;&minus; 1]。本题中，如果除法结果溢出，则返回 231&nbsp;&minus; 1。


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def divide(self, dividend: int, divisor: int) -> int:

        # 被除数为最小值
        INT_MIN, INT_MAX = -2**31, 2**31-1
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX

        # 除数为最小值
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0

        # 被除数为 0
        if dividend == 0:
            return 0

        # 类二分查找
        # 正数取相反数
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev

        candidates = [divisor]
        # 注意溢出
        while candidates[-1] >= dividend - candidates[-1]:
            candidates.append(candidates[-1] + candidates[-1])

        ans = 0
        for i in range(len(candidates) - 1, -1, -1):
            if candidates[i] >= dividend:
                ans += (1 << i)
                dividend -= candidates[i]

        return -ans if rev else ans


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(0, self.inst.divide(100, 23))


if __name__ == "__main__":
    unittest.main()
