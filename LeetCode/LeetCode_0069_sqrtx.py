#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-01 17:57:09

# 导入所需的依赖库
import unittest

# 题目编号: 69
# 题目名称: x 的平方根 
# 题目难度: Easy

# 知识点: 数学, 二分查找

# 题目详情:
"""
给你一个非负整数 x ，计算并返回&nbsp;x&nbsp;的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

&nbsp;

示例 1：


输入：x = 4
输出：2


示例 2：


输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。


&nbsp;

提示：


	0 &lt;= x &lt;= 231 - 1


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
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
