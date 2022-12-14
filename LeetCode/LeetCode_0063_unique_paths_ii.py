#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-14 17:11:15

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 63
# 题目名称: 不同路径 II
# 题目难度: Medium

# 知识点: 数组, 动态规划, 矩阵

# 题目详情:
"""
一个机器人位于一个&nbsp;m x n&nbsp;网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

&nbsp;

示例 1：


输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -&gt; 向右 -&gt; 向下 -&gt; 向下
2. 向下 -&gt; 向下 -&gt; 向右 -&gt; 向右


示例 2：


输入：obstacleGrid = [[0,1],[0,0]]
输出：1


&nbsp;

提示：


	m ==&nbsp;obstacleGrid.length
	n ==&nbsp;obstacleGrid[i].length
	1 &lt;= m, n &lt;= 100
	obstacleGrid[i][j] 为 0 或 1


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        # dp = [[1] * cols] + [[1] + [0] * (cols - 1) for _ in range(rows - 1)]
        dp = [[0] * cols for _ in range(rows)]

        for i in range(cols):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1

        for i in range(rows):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for i in range(1, rows):
            for j in range(1, cols):

                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

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
        self.assertEqual(2, self.inst.uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))


if __name__ == "__main__":
    unittest.main()
