#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-05 10:18:41

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 41
# 题目名称: 缺失的第一个正数
# 题目难度: Hard

# 知识点: 数组, 哈希表

# 题目详情:
"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

 

示例 1：


输入：nums = [1,2,0]
输出：3


示例 2：


输入：nums = [3,4,-1,1]
输出：2


示例 3：


输入：nums = [7,8,9,11,12]
输出：1


 

提示：


	1 5
	-231 31 - 1


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


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
