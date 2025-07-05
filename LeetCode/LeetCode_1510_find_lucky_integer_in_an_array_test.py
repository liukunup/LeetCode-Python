#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2025-07-05 10:04:00

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 1510
# 题目名称: 找出数组中的幸运数
# 题目难度: Easy

# 知识点: 数组, 哈希表, 计数

# 题目详情:
"""
在整数数组中，如果一个整数的出现频次和它的数值大小相等，我们就称这个整数为「幸运数」。

给你一个整数数组 arr，请你从中找出并返回一个幸运数。


	如果数组中存在多个幸运数，只需返回 最大 的那个。
	如果数组中不含幸运数，则返回 -1 。


&nbsp;

示例 1：

输入：arr = [2,2,3,4]
输出：2
解释：数组中唯一的幸运数是 2 ，因为数值 2 的出现频次也是 2 。


示例 2：

输入：arr = [1,2,2,3,3,3]
输出：3
解释：1、2 以及 3 都是幸运数，只需要返回其中最大的 3 。


示例 3：

输入：arr = [2,2,2,3,3]
输出：-1
解释：数组中不存在幸运数。


示例 4：

输入：arr = [5]
输出：-1


示例 5：

输入：arr = [7,7,7,7,7,7,7]
输出：7


&nbsp;

提示：


	1 &lt;= arr.length &lt;= 500
	1 &lt;= arr[i] &lt;= 500


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        count_tab = dict()
        for val in arr:
            if val in count_tab:
                count_tab[val] += 1
            else:
                count_tab[val] = 1
        for k, v in count_tab.items():
            if k == v:
                ans = max(ans, k)
        return ans


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(3, self.inst.findLucky([1,2,2,3,3,3]))


if __name__ == "__main__":
    unittest.main()
