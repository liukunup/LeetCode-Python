#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-29 10:29:12

# 导入所需的依赖库
import unittest
from itertools import chain

# 题目编号: 6
# 题目名称: Z 字形变换
# 题目难度: Medium

# 知识点: 字符串

# 题目详情:

"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：


P   A   H   N
A P L S I I G
Y   I   R

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：


string convert(string s, int numRows);

 

示例 1：


输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

示例 2：


输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I


示例 3：


输入：s = "A", numRows = 1
输出："A"


 

提示：


	1 
	s 由英文字母（小写和大写）、',' 和 '.' 组成
	1 


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def convert(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s

        t = 2 * r - 2
        c = (n + t - 1) // t * (r - 1)
        mat = [[''] * c for _ in range(r)]
        x, y = 0, 0
        for i, ch in enumerate(s):
            mat[x][y] = ch
            if i % t < r - 1:
                x += 1
            else:
                x -= 1
                y += 1
        return ''.join(ch for row in mat for ch in row if ch)

    def convert_v2(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s

        mat = [[] for _ in range(r)]
        t, x = 2 * r - 2, 0
        for i, ch in enumerate(s):
            mat[x].append(ch)
            x += 1 if i % t < r - 1 else -1
        return ''.join(chain(*mat))

    def convert_v3(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s

        t = 2 * r - 2
        ans = []
        for i in range(r):
            for j in range(0, n - i, t):
                ans.append(s[j + i])
                if 0 < i < r - 1 and j + t - i < n:
                    ans.append(s[j + t - i])

        return ''.join(ans)


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
