#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-14 11:53:15

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 57
# 题目名称: 插入区间
# 题目难度: Medium

# 知识点: 数组

# 题目详情:
"""
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

 

示例 1：


输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]


示例 2：


输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

示例 3：


输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]


示例 4：


输入：intervals = [[1,5]], newInterval = [2,3]
输出：[[1,5]]


示例 5：


输入：intervals = [[1,5]], newInterval = [2,7]
输出：[[1,7]]


 

提示：


	0 4
	intervals[i].length == 2
	0 5
	intervals 根据 intervals[i][0] 按 升序 排列
	newInterval.length == 2
	0 5


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        done = False
        res = list()

        for cur_left, cur_right in intervals:
            if right < cur_left:
                if not done:
                    res.append([left, right])
                    done = True
                res.append([cur_left, cur_right])
            elif left > cur_right:
                res.append([cur_left, cur_right])
            else:
                left = min(left, cur_left)
                right = max(right, cur_right)

        if not done:
            res.append([left, right])

        return res

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
