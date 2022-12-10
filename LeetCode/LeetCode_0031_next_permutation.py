#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-10 22:17:28

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 31
# 题目名称: 下一个排列
# 题目难度: Medium

# 知识点: 数组, 双指针

# 题目详情:
"""
整数数组的一个 排列&nbsp; 就是将其所有成员以序列或线性顺序排列。


	例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。


整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。


	例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
	类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
	而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。


给你一个整数数组 nums ，找出 nums 的下一个排列。

必须 原地 修改，只允许使用额外常数空间。

&nbsp;

示例 1：


输入：nums = [1,2,3]
输出：[1,3,2]


示例 2：


输入：nums = [3,2,1]
输出：[1,2,3]


示例 3：


输入：nums = [1,1,5]
输出：[1,5,1]


&nbsp;

提示：


	1 &lt;= nums.length &lt;= 100
	0 &lt;= nums[i] &lt;= 100


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 反向寻找降序点
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # 找swap值
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # 子序列反序
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


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
