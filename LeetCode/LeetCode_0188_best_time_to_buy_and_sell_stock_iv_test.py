#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2025-08-24 22:03:08

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 188
# 题目名称: 买卖股票的最佳时机 IV
# 题目难度: Hard

# 知识点: 数组, 动态规划

# 题目详情:
"""
给你一个整数数组&nbsp;prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

&nbsp;

示例 1：


输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

示例 2：


输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

&nbsp;

提示：


	1 &lt;= k &lt;= 100
	1 &lt;= prices.length &lt;= 1000
	0 &lt;= prices[i] &lt;= 1000


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0]*k for _ in range(n)]
        dp[0] = [-prices[0], 0]*k
        for i in range(1, n):
            for j in range(k):
                dp[i][j*2]   = max(dp[i-1][j*2],   -prices[i] + (dp[i-1][j*2-1] if j!=0 else 0))
                dp[i][j*2+1] = max(dp[i-1][j*2+1], +prices[i] +  dp[i-1][j*2])
        return dp[-1][-1]


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(self.inst.maxProfit(k = 2, prices = [3,2,6,5,0,3]), 7)


if __name__ == "__main__":
    unittest.main()
