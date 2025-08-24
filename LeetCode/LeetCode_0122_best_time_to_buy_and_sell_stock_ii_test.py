#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2025-08-24 21:25:36

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 122
# 题目名称: 买卖股票的最佳时机 II
# 题目难度: Medium

# 知识点: 贪心, 数组, 动态规划

# 题目详情:
"""
给你一个整数数组 prices ，其中&nbsp;prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候&nbsp;最多&nbsp;只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润&nbsp;。

&nbsp;

示例 1：


输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3。
最大总利润为 4 + 3 = 7 。

示例 2：


输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
最大总利润为 4 。

示例&nbsp;3：


输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0。

&nbsp;

提示：


	1 &lt;= prices.length &lt;= 3 * 104
	0 &lt;= prices[i] &lt;= 104


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(self.inst.maxProfit(prices = [7,1,5,3,6,4]), 7)


if __name__ == "__main__":
    unittest.main()
