#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-13 18:57:35

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 54
# 题目名称: 螺旋矩阵
# 题目难度: Medium

# 知识点: 数组, 矩阵, 模拟

# 题目详情:
"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

 

示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]


示例 2：


输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


 

提示：


	m == matrix.length
	n == matrix[i].length
	1 
	-100 


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m, n = len(matrix), len(matrix[0])

        top, bottom, left, right = 0, m - 1, 0, n - 1

        res = list()

        while True:
            res.extend([matrix[top][index] for index in range(left, right + 1, 1)])
            top += 1
            if top > bottom:
                break

            res.extend([matrix[index][right] for index in range(top, bottom + 1, 1)])
            right -= 1
            if right < left:
                break

            res.extend([matrix[bottom][index] for index in range(right, left - 1, -1)])
            bottom -= 1
            if bottom < top:
                break

            res.extend([matrix[index][left] for index in range(bottom, top - 1, -1)])
            left += 1
            if left > right:
                break

        return res


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual([1,2,3,6,9,8,7,4,5], self.inst.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))


if __name__ == "__main__":
    unittest.main()
