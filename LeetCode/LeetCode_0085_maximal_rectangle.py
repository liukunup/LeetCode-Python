#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-28 16:36:27

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 85
# 题目名称: 最大矩形
# 题目难度: Hard

# 知识点: 栈, 数组, 动态规划, 矩阵, 单调栈

# 题目详情:
"""
给定一个仅包含&nbsp;0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

&nbsp;

示例 1：


输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。


示例 2：


输入：matrix = []
输出：0


示例 3：


输入：matrix = [["0"]]
输出：0


示例 4：


输入：matrix = [["1"]]
输出：1


示例 5：


输入：matrix = [["0","0"]]
输出：0


&nbsp;

提示：


	rows == matrix.length
	cols == matrix[0].length
	1 &lt;= row, cols &lt;= 200
	matrix[i][j] 为 '0' 或 '1'


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if j == 0:
                    matrix[i][j] = int(matrix[i][j])
                else:
                    matrix[i][j] = matrix[i][j - 1] + 1 if matrix[i][j] == '1' else 0
        ans = 0
        for j in range(n):
            stack = list()
            left = [-1] * m
            right = [m] * m
            for i in range(m):
                while stack and matrix[stack[-1]][j] > matrix[i][j]:
                    right[stack[-1]] = i
                    stack.pop()
                left[i] = stack[-1] if stack else -1
                stack.append(i)
            tmp = max((right[i] - left[i] - 1) * matrix[i][j] for i in range(m))
            ans = max(ans, tmp)
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
        self.assertEqual(6, self.inst.maximalRectangle(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))


if __name__ == "__main__":
    unittest.main()
