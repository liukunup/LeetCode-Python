#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-01 18:07:17

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 66
# 题目名称: 加一
# 题目难度: Easy

# 知识点: 数组, 数学

# 题目详情:
"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

 

示例 1：


输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。


示例 2：


输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。


示例 3：


输入：digits = [0]
输出：[1]


 

提示：


	1 
	0 


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        carry = 1
        for i in range(n, -1, -1):

            if carry == 1 and digits[i] == 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1
                carry = 0

            if carry == 0: break

        if carry == 1:
            digits = [1] + digits

        return digits


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual(self.inst.plusOne(digits=[4, 3, 2, 1]), [4,3,2,2])

    def test_2(self):
        self.assertEqual(self.inst.plusOne(digits=[9, 9, 9]), [1,0,0,0])


if __name__ == "__main__":
    unittest.main()
