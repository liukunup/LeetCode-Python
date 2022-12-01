#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-01 19:16:01

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 53
# 题目名称: 最大子数组和
# 题目难度: Medium

# 知识点: 数组, 分治, 动态规划

# 题目详情:
"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。

&nbsp;

示例 1：


输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组&nbsp;[4,-1,2,1] 的和最大，为&nbsp;6 。


示例 2：


输入：nums = [1]
输出：1


示例 3：


输入：nums = [5,4,-1,7,8]
输出：23


&nbsp;

提示：


	1 &lt;= nums.length &lt;= 105
	-104 &lt;= nums[i] &lt;= 104


&nbsp;

进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。

"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


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
