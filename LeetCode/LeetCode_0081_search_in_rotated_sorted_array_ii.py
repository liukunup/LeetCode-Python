#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-15 17:30:46

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 81
# 题目名称: 搜索旋转排序数组 II
# 题目难度: Medium

# 知识点: 数组, 二分查找

# 题目详情:
"""
已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

在传递给函数之前，nums 在预先未知的某个下标 k（0 &lt;= k &lt; nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。

你必须尽可能减少整个操作步骤。

&nbsp;

示例&nbsp;1：


输入：nums = [2,5,6,0,0,1,2], target = 0
输出：true


示例&nbsp;2：


输入：nums = [2,5,6,0,0,1,2], target = 3
输出：false

&nbsp;

提示：


	1 &lt;= nums.length &lt;= 5000
	-104 &lt;= nums[i] &lt;= 104
	题目数据保证 nums 在预先未知的某个下标上进行了旋转
	-104 &lt;= target &lt;= 104


&nbsp;

进阶：


	这是 搜索旋转排序数组&nbsp;的延伸题目，本题中的&nbsp;nums&nbsp; 可能包含重复元素。
	这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？


&nbsp;

"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        if not nums:
            return False

        n = len(nums)
        if n == 1:
            return nums[0] == target

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[n - 1]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(True, self.inst.search(nums=[2,5,6,0,0,1,2], target=0))


if __name__ == "__main__":
    unittest.main()
