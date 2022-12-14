#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-14 10:31:40

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 55
# 题目名称: 跳跃游戏
# 题目难度: Medium

# 知识点: 贪心, 数组, 动态规划

# 题目详情:
"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

 

示例 1：


输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。


示例 2：


输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。


 

提示：


	1 4
	0 5


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0
        for i in range(len(nums)):
            if i <= max_pos:
                max_pos = max(max_pos, i + nums[i])
                if max_pos >= len(nums) - 1:
                    return True
        return False


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual(True, self.inst.canJump(nums = [2,3,1,1,4]))

    def test_2(self):
        self.assertEqual(False, self.inst.canJump(nums = [3,2,1,0,4]))

    def test_3(self):
        self.assertEqual(True, self.inst.canJump(nums = [1,2]))

    def test_4(self):
        self.assertEqual(False, self.inst.canJump(nums=[0, 2, 3]))


if __name__ == "__main__":
    unittest.main()
