#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-30 20:17:01

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 18
# 题目名称: 四数之和
# 题目难度: Medium

# 知识点: 数组, 双指针, 排序

# 题目详情:
"""
给你一个由 n 个整数组成的数组&nbsp;nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组&nbsp;[nums[a], nums[b], nums[c], nums[d]]&nbsp;（若两个四元组元素一一对应，则认为两个四元组重复）：


	0 &lt;= a, b, c, d&nbsp;&lt; n
	a、b、c 和 d 互不相同
	nums[a] + nums[b] + nums[c] + nums[d] == target


你可以按 任意顺序 返回答案 。

&nbsp;

示例 1：


输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


示例 2：


输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]


&nbsp;

提示：


	1 &lt;= nums.length &lt;= 200
	-109 &lt;= nums[i] &lt;= 109
	-109 &lt;= target &lt;= 109


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = list()
        if not nums or len(nums) < 4:
            return res

        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual(self.inst.fourSum(nums=[2,2,2,2,2], target=8), [])


if __name__ == "__main__":
    unittest.main()
