#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-13 10:24:53

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 33
# 题目名称: 搜索旋转排序数组
# 题目难度: Medium

# 知识点: 数组, 二分查找

# 题目详情:
"""
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 &lt;= k &lt; nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为&nbsp;[4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回&nbsp;-1&nbsp;。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

&nbsp;

示例 1：


输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4


示例&nbsp;2：


输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：


输入：nums = [1], target = 0
输出：-1


&nbsp;

提示：


	1 &lt;= nums.length &lt;= 5000
	-104 &lt;= nums[i] &lt;= 104
	nums 中的每个值都 独一无二
	题目数据保证 nums 在预先未知的某个下标上进行了旋转
	-104 &lt;= target &lt;= 104


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if (nums[0] > nums[mid]) ^ (target > nums[mid]) ^ (nums[0] > target):
                left = mid + 1
            else:
                right = mid
        return left if left == right and nums[left] == target else -1


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(4, self.inst.search(nums=[4,5,6,7,0,1,2], target=0))


if __name__ == "__main__":
    unittest.main()
