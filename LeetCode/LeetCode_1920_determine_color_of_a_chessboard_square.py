#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-08 11:37:49

# 导入所需的依赖库
import unittest

# 题目编号: 1920
# 题目名称: 判断国际象棋棋盘中一个格子的颜色
# 题目难度: Easy

# 知识点: 数学, 字符串

# 题目详情:
"""
给你一个坐标 coordinates ，它是一个字符串，表示国际象棋棋盘中一个格子的坐标。下图是国际象棋棋盘示意图。



如果所给格子的颜色是白色，请你返回 true，如果是黑色，请返回 false 。

给定坐标一定代表国际象棋棋盘上一个存在的格子。坐标第一个字符是字母，第二个字符是数字。

 

示例 1：


输入：coordinates = "a1"
输出：false
解释：如上图棋盘所示，"a1" 坐标的格子是黑色的，所以返回 false 。


示例 2：


输入：coordinates = "h3"
输出：true
解释：如上图棋盘所示，"h3" 坐标的格子是白色的，所以返回 true 。


示例 3：


输入：coordinates = "c7"
输出：false


 

提示：


	coordinates.length == 2
	'a' 
	'1' 


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) - ord('a') + 1 + int(coordinates[1])) % 2 == 1


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
