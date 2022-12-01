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

    def maxSubArray_v2(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        return self.__max_sub_array(nums, 0, size - 1)

    def __max_sub_array(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) >> 1
        return max(self.__max_sub_array(nums, left, mid),
                   self.__max_sub_array(nums, mid + 1, right),
                   self.__max_cross_array(nums, left, mid, right))


    def __max_cross_array(self, nums, left, mid, right):
        # 一定包含 nums[mid] 元素的最大连续子数组的和，
        # 思路是看看左边"扩散到底"，得到一个最大数，右边"扩散到底"得到一个最大数
        # 然后再加上中间数
        left_sum_max = 0
        start_left = mid - 1
        s1 = 0
        while start_left >= left:
            s1 += nums[start_left]
            left_sum_max = max(left_sum_max, s1)
            start_left -= 1

        right_sum_max = 0
        start_right = mid + 1
        s2 = 0
        while start_right <= right:
            s2 += nums[start_right]
            right_sum_max = max(right_sum_max, s2)
            start_right += 1
        return left_sum_max + nums[mid] + right_sum_max


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
