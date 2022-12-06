#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-06 11:54:43

# 导入所需的依赖库
import copy
import unittest
from typing import List

# 题目编号: 89
# 题目名称: 格雷编码
# 题目难度: Medium

# 知识点: 位运算, 数学, 回溯

# 题目详情:
"""
n 位格雷码序列 是一个由 2n 个整数组成的序列，其中：

	每个整数都在范围 [0, 2n - 1] 内（含 0 和 2n - 1）
	第一个整数是 0
	一个整数在序列中出现 不超过一次
	每对 相邻 整数的二进制表示 恰好一位不同 ，且
	第一个 和 最后一个 整数的二进制表示 恰好一位不同


给你一个整数 n ，返回任一有效的 n 位格雷码序列 。

&nbsp;

示例 1：


输入：n = 2
输出：[0,1,3,2]
解释：
[0,1,3,2] 的二进制表示是 [00,01,11,10] 。
- 00 和 01 有一位不同
- 01 和 11 有一位不同
- 11 和 10 有一位不同
- 10 和 00 有一位不同
[0,2,3,1] 也是一个有效的格雷码序列，其二进制表示是 [00,10,11,01] 。
- 00 和 10 有一位不同
- 10 和 11 有一位不同
- 11 和 01 有一位不同
- 01 和 00 有一位不同


示例 2：


输入：n = 1
输出：[0,1]


&nbsp;

提示：


	1 &lt;= n &lt;= 16


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def grayCode(self, n: int) -> List[int]:
        # 会超时的
        # 虽然只要求返回一组，但是我们试试找全
        solutions = list()
        # 位运算判定字典
        dic = [1 << j for j in range(n)]

        def backtrace(nums: List[int]):
            # 满足条件
            if len(nums) == pow(2, n):
                solutions.append(copy.deepcopy(nums))
                return
            # 继续搜索 因为已经从0开始了，所以可以少搜索一个0，从1开始
            for i in range(1, pow(2, n)):
                # 约束条件: 数字已经被使用
                if i in nums:
                    continue
                # 约束条件: 当前下标为i的数字(其实就是这个树) 是满足要求的
                if i ^ nums[-1] in dic:
                    # 约束条件: 如果是最后一个数字 需要和第一个0做判断
                    if len(nums) == pow(2, n) - 1:
                        if i ^ 0 in dic:
                            backtrace(nums + [i])
                    else:
                        backtrace(nums + [i])

        # 初始条件: 第一个整数是 0
        backtrace([0])

        return [] if not solutions else solutions[0]

    def grayCode_v2(self, n: int) -> List[int]:
        # 初始情况
        solution = [0] * (1 << n)
        # 移位异或
        for i in range(1 << n):
            solution[i] = (i >> 1) ^ i
        return solution


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual([0, 1], self.inst.grayCode_v2(1))

    def test_2(self):
        self.assertEqual([0, 1, 3, 2], self.inst.grayCode_v2(2))

    def test_3(self):
        self.assertEqual([0, 1, 3, 2, 6, 7, 5, 4], self.inst.grayCode_v2(3))


if __name__ == "__main__":
    unittest.main()
