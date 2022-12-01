#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-30 20:34:40

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 88
# 题目名称: 合并两个有序数组
# 题目难度: Easy

# 知识点: 数组, 双指针, 排序

# 题目详情:
"""
给你两个按 非递减顺序 排列的整数数组&nbsp;nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

&nbsp;

示例 1：


输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。


示例 2：


输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。


示例 3：


输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。


&nbsp;

提示：


	nums1.length == m + n
	nums2.length == n
	0 &lt;= m, n &lt;= 200
	1 &lt;= m + n &lt;= 200
	-109 &lt;= nums1[i], nums2[j] &lt;= 109


&nbsp;

进阶：你可以设计实现一个时间复杂度为 O(m + n) 的算法解决此问题吗？

"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        p_end = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[p_end] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[p_end] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[p_end] = nums1[p1]
                p1 -= 1
            else:
                nums1[p_end] = nums2[p2]
                p2 -= 1
            p_end -= 1


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
