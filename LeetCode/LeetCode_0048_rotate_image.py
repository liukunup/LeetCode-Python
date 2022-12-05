#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-05 16:52:29

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 48
# 题目名称: 旋转图像
# 题目难度: Medium

# 知识点: 数组, 数学, 矩阵

# 题目详情:
"""
给定一个 n&nbsp;×&nbsp;n 的二维矩阵&nbsp;matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

&nbsp;

示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]


示例 2：


输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


&nbsp;

提示：


	n == matrix.length == matrix[i].length
	1 &lt;= n &lt;= 20
	-1000 &lt;= matrix[i][j] &lt;= 1000


&nbsp;

"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 交换矩阵行
        row_begin, row_end = 0, len(matrix) - 1
        while row_begin < row_end:
            tmp = matrix[row_begin]
            matrix[row_begin] = matrix[row_end]
            matrix[row_end] = tmp
            row_begin += 1
            row_end -= 1

        # 矩阵镜像
        n = len(matrix)
        for i in range(n):
            for j in range(0, i, 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp


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
