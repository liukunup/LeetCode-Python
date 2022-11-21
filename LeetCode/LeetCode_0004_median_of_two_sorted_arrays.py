#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-21 15:12:50

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 4
# 题目名称: 寻找两个正序数组的中位数
# 题目难度: Hard

# 知识点: 数组, 二分查找, 分治

# 题目详情:
"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组&nbsp;nums1 和&nbsp;nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

&nbsp;

示例 1：


输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2


示例 2：


输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5


&nbsp;

&nbsp;

提示：


	nums1.length == m
	nums2.length == n
	0 &lt;= m &lt;= 1000
	0 &lt;= n &lt;= 1000
	1 &lt;= m + n &lt;= 2000
	-106 &lt;= nums1[i], nums2[i] &lt;= 106


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 存储合并后的数组
        nums = list()
        # 获取长度
        n1 = len(nums1)
        n2 = len(nums2)
        # 判空
        if n1 == 0:
            # 判奇偶
            if n2 % 2 == 0:
                return (nums2[int(n2 / 2 - 1)] + nums2[int(n2 / 2)]) / 2.0
            else:
                return nums2[int(n2 / 2)]
        if n2 == 0:
            # 判奇偶
            if n1 % 2 == 0:
                return (nums1[int(n1 / 2 - 1)] + nums1[int(n1 / 2)]) / 2.0
            else:
                return nums1[int(n1 / 2)]
        # 升序归并
        count = 0
        i, j = 0, 0
        while count != n1 + n2:
            # 某一个列表遍历完成
            if i == n1:
                while j != n2:
                    nums.append(nums2[j])
                    j += 1
                    count += 1
                break
            if j == n2:
                while i != n1:
                    nums.append(nums1[i])
                    i += 1
                    count += 1
                break
            # 双指针各自遍历做归并
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
                count += 1
            else:
                nums.append(nums2[j])
                j += 1
                count += 1
        # 计算中位数 判奇偶
        if count % 2 == 0:
            return (nums[int(count / 2 - 1)] + nums[int(count / 2)]) / 2.0
        else:
            return nums[int(count / 2)]


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        num_list_1 = [1, 3]
        num_list_2 = [2]
        self.assertEqual(self.inst.findMedianSortedArrays(num_list_1, num_list_2), 2.0)

    def test_2(self):
        num_list_1 = [1, 2]
        num_list_2 = [3, 4]
        self.assertEqual(self.inst.findMedianSortedArrays(num_list_1, num_list_2), 2.5)


if __name__ == "__main__":
    unittest.main()
