#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-15 15:53:58

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 79
# 题目名称: 单词搜索
# 题目难度: Medium

# 知识点: 数组, 回溯, 矩阵

# 题目详情:
"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例 1：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true


示例 2：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true


示例 3：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false


 

提示：


	m == board.length
	n = board[i].length
	1 
	1 
	board 和 word 仅由大小写英文字母组成


 

进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？

"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(ii, jj, kk) -> bool:
            #
            if board[ii][jj] != word[kk]:
                return False
            #
            if kk == len(word) - 1:
                return True

            #
            result = False
            visited.add((ii, jj))
            for di, dj in directions:
                ni, nj = ii + di, jj + dj
                if 0 <= ni < h and 0 <= nj < w and (ni, nj) not in visited:
                    if check(ni, nj, kk + 1):
                        result = True
                        break
            visited.remove((ii, jj))
            return result

        #
        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
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
        self.assertEqual(0, -1)


if __name__ == "__main__":
    unittest.main()
