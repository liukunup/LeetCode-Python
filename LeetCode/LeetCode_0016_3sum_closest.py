#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-27 13:30:45

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 16
# 题目名称: 最接近的三数之和
# 题目难度: Medium

# 知识点: 数组, 双指针, 排序

# 题目详情:
"""
给你一个长度为 n 的整数数组&nbsp;nums&nbsp;和 一个目标值&nbsp;target。请你从 nums 中选出三个整数，使它们的和与&nbsp;target&nbsp;最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

&nbsp;

示例 1：


输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。


示例 2：


输入：nums = [0,0,0], target = 1
输出：0


&nbsp;

提示：


	3 &lt;= nums.length &lt;= 1000
	-1000 &lt;= nums[i] &lt;= 1000
	-104 &lt;= target &lt;= 104


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10**7

        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                update(s)
                if s > target:
                    k0 = k - 1
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    j0 = j + 1
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0

        return best


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual(self.inst.threeSumClosest([-1, 2, 1, -4], 1), 2)

    def test_2(self):
        self.assertEqual(self.inst.threeSumClosest([0, 0, 0], 1), 0)


if __name__ == "__main__":
    unittest.main()
