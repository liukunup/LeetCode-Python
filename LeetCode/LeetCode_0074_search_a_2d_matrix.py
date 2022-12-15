#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-15 11:54:10

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 74
# 题目名称: 搜索二维矩阵
# 题目难度: Medium

# 知识点: 数组, 二分查找, 矩阵

# 题目详情:
"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：


	每行中的整数从左到右按升序排列。
	每行的第一个整数大于前一行的最后一个整数。


 

示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true


示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false


 

提示：


	m == matrix.length
	n == matrix[i].length
	1 
	-104 4


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        while top < bottom:
            mid = (top + bottom) // 2

            if target < matrix[mid][left]:
                bottom = mid - 1
            elif target > matrix[mid][right]:
                top = mid + 1
            elif target in matrix[mid]:
                return True

        while left < right:
            mid = (left + right) // 2

            if target < matrix[top][mid]:
                right = mid - 1
            elif target > matrix[top][mid]:
                left = mid + 1
            elif target == matrix[top][mid]:
                return True

        return False

    def searchMatrix_v2(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        beg, end = 0, rows * cols - 1
        while beg <= end:
            mid = (beg + end) // 2
            value = matrix[mid // cols][mid % cols]
            if target < value:
                end = mid - 1
            elif target > value:
                beg = mid + 1
            else:
                return True

        return False





# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(True, self.inst.searchMatrix_v2(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))


if __name__ == "__main__":
    unittest.main()
