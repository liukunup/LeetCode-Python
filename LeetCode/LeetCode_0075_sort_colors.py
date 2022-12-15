#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-15 15:08:27

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 75
# 题目名称: 颜色分类
# 题目难度: Medium

# 知识点: 数组, 双指针, 排序

# 题目详情:
"""
给定一个包含红色、白色和蓝色、共&nbsp;n 个元素的数组&nbsp;nums&nbsp;，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、&nbsp;1 和 2 分别表示红色、白色和蓝色。




必须在不使用库内置的 sort 函数的情况下解决这个问题。

&nbsp;

示例 1：


输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]


示例 2：


输入：nums = [2,0,1]
输出：[0,1,2]


&nbsp;

提示：


	n == nums.length
	1 &lt;= n &lt;= 300
	nums[i] 为 0、1 或 2


&nbsp;

进阶：


	你能想出一个仅使用常数空间的一趟扫描算法吗？


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.inst.sortColors(nums=[2, 0, 2, 1, 1, 0])


if __name__ == "__main__":
    unittest.main()
