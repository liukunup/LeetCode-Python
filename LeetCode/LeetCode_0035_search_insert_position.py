#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-29 17:44:21

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 35
# 题目名称: 搜索插入位置
# 题目难度: Easy

# 知识点: 数组, 二分查找

# 题目详情:
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

&nbsp;

示例 1:


输入: nums = [1,3,5,6], target = 5
输出: 2


示例&nbsp;2:


输入: nums = [1,3,5,6], target = 2
输出: 1


示例 3:


输入: nums = [1,3,5,6], target = 7
输出: 4


&nbsp;

提示:


	1 &lt;= nums.length &lt;= 104
	-104 &lt;= nums[i] &lt;= 104
	nums 为&nbsp;无重复元素&nbsp;的&nbsp;升序&nbsp;排列数组
	-104 &lt;= target &lt;= 104


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual(self.inst.searchInsert([1,3,5,6], 5), 2)

    def test_2(self):
        self.assertEqual(self.inst.searchInsert([1,3,5,6], 2), 1)

    def test_3(self):
        self.assertEqual(self.inst.searchInsert([1,3,5,6], 7), 4)


if __name__ == "__main__":
    unittest.main()
