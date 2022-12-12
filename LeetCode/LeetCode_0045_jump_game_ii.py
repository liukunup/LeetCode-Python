#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-12 17:22:57

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 45
# 题目名称: 跳跃游戏 II
# 题目难度: Medium

# 知识点: 贪心, 数组, 动态规划

# 题目详情:
"""
给你一个非负整数数组 nums ，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

假设你总是可以到达数组的最后一个位置。

 

示例 1:


输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。


示例 2:


输入: nums = [2,3,0,1,4]
输出: 2


 

提示:


	1 4
	0 


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def jump(self, nums: List[int]) -> int:
        pos = len(nums) - 1
        steps = 0

        while pos > 0:
            for i in range(0, pos):
                if i + nums[i] >= pos:
                    pos = i
                    steps += 1
                    break

        return steps

    def jump_v2(self, nums: List[int]) -> int:
        n = len(nums)
        max_pos, end, steps = 0, 0, 0
        for i in range(n - 1):
            if max_pos >= i:
                max_pos = max(max_pos, i + nums[i])
                if i == end:
                    end = max_pos
                    steps += 1
        return steps


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(2, self.inst.jump_v2(nums=[2,3,1,1,4]))


if __name__ == "__main__":
    unittest.main()
