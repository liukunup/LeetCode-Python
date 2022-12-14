#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-14 17:45:56

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 64
# 题目名称: 最小路径和
# 题目难度: Medium

# 知识点: 数组, 动态规划, 矩阵

# 题目详情:
"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

 

示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。


示例 2：


输入：grid = [[1,2,3],[4,5,6]]
输出：12


 

提示：


	m == grid.length
	n == grid[i].length
	1 
	0 


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]

        dp[0][0] = grid[0][0]

        for i in range(1, cols):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

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
        self.assertEqual(0, -1)


if __name__ == "__main__":
    unittest.main()
