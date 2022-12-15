#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-15 11:36:13

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 73
# 题目名称: 矩阵置零
# 题目难度: Medium

# 知识点: 数组, 哈希表, 矩阵

# 题目详情:
"""
给定一个&nbsp;m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。




&nbsp;

示例 1：


输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]


示例 2：


输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]


&nbsp;

提示：


	m == matrix.length
	n == matrix[0].length
	1 &lt;= m, n &lt;= 200
	-231 &lt;= matrix[i][j] &lt;= 231 - 1


&nbsp;

进阶：


	一个直观的解决方案是使用 &nbsp;O(mn)&nbsp;的额外空间，但这并不是一个好的解决方案。
	一个简单的改进方案是使用 O(m&nbsp;+&nbsp;n) 的额外空间，但这仍然不是最好的解决方案。
	你能想出一个仅使用常量空间的解决方案吗？


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])

        z_row = [False] * rows
        z_col = [False] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    z_row[i] = True
                    z_col[j] = True

        for i, z in enumerate(z_row):
            if z:
                for j in range(cols):
                    matrix[i][j] = 0

        for i, z in enumerate(z_col):
            if z:
                for j in range(rows):
                    matrix[j][i] = 0


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
