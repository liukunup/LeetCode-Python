#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-14 11:03:36

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 56
# 题目名称: 合并区间
# 题目难度: Medium

# 知识点: 数组, 排序

# 题目详情:
"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回&nbsp;一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间&nbsp;。

&nbsp;

示例 1：


输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].


示例&nbsp;2：


输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

&nbsp;

提示：


	1 &lt;= intervals.length &lt;= 104
	intervals[i].length == 2
	0 &lt;= starti &lt;= endi &lt;= 104


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual([[1,6],[8,10],[15,18]], self.inst.merge(intervals = [[2,6],[1,3],[8,10],[15,18]]))

    def test_2(self):
        self.assertEqual([[0, 5]], self.inst.merge(intervals=[[1, 4], [0, 2], [3, 5]]))

    def test_3(self):
        self.assertEqual([[0, 4]], self.inst.merge(intervals=[[1,4],[0,4]]))

    def test_4(self):
        self.assertEqual([[1, 4]], self.inst.merge(intervals=[[1,4],[2,3]]))


if __name__ == "__main__":
    unittest.main()
