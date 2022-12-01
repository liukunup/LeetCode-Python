#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-01 11:07:20

# 导入所需的依赖库
import unittest

# 题目编号: 70
# 题目名称: 爬楼梯
# 题目难度: Easy

# 知识点: 记忆化搜索, 数学, 动态规划

# 题目详情:
"""
假设你正在爬楼梯。需要 n&nbsp;阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

&nbsp;

示例 1：


输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：


输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶


&nbsp;

提示：


	1 &lt;= n &lt;= 45


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def climbStairs(self, n: int) -> int:
        # f(x-2) f(x-1) f(x)
        p, q, r = 0, 0, 1
        for i in range(n):
            p = q
            q = r
            r = p + q
        return r


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
