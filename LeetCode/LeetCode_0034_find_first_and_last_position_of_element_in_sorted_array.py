#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-13 11:04:17

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 34
# 题目名称: 在排序数组中查找元素的第一个和最后一个位置
# 题目难度: Medium

# 知识点: 数组, 二分查找

# 题目详情:
"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回&nbsp;[-1, -1]。

你必须设计并实现时间复杂度为&nbsp;O(log n)&nbsp;的算法解决此问题。

&nbsp;

示例 1：


输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例&nbsp;2：


输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：


输入：nums = [], target = 0
输出：[-1,-1]

&nbsp;

提示：


	0 &lt;= nums.length &lt;= 105
	-109&nbsp;&lt;= nums[i]&nbsp;&lt;= 109
	nums&nbsp;是一个非递减数组
	-109&nbsp;&lt;= target&nbsp;&lt;= 109


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        if len(nums) == 1:
            return [0, 0] if target in nums else [-1, -1]


        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid
            else:
                beg, end = mid, mid
                while beg >= 0 and nums[beg] == nums[mid]:
                    beg -= 1
                while end < len(nums) and nums[end] == nums[mid]:
                    end += 1
                return [beg + 1, end - 1]
        return [left, right] if left == right and nums[left] == target else [-1, -1]


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual([3,4], self.inst.searchRange(nums=[5,7,7,8,8,10], target=8))

    def test_2(self):
        self.assertEqual([1,1], self.inst.searchRange(nums=[1, 4], target=4))


if __name__ == "__main__":
    unittest.main()
