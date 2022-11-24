#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-24 23:37:38

# 导入所需的依赖库
import unittest

# 题目编号: 12
# 题目名称: 整数转罗马数字
# 题目难度: Medium

# 知识点: 哈希表, 数学, 字符串

# 题目详情:
"""
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。


字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：


	I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
	X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
	C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。


给你一个整数，将其转为罗马数字。

 

示例 1:


输入: num = 3
输出: "III"

示例 2:


输入: num = 4
输出: "IV"

示例 3:


输入: num = 9
输出: "IX"

示例 4:


输入: num = 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.


示例 5:


输入: num = 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.

 

提示：


	1 


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    VALUE_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    def intToRoman(self, num: int) -> str:
        roman = list()
        for value, symbol in self.VALUE_SYMBOLS:
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0:
                break
        return "".join(roman)


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual(self.inst.intToRoman(3), "III")

    def test_2(self):
        self.assertEqual(self.inst.intToRoman(4), "IV")

    def test_3(self):
        self.assertEqual(self.inst.intToRoman(58), "LVIII")

    def test_4(self):
        self.assertEqual(self.inst.intToRoman(1994), "MCMXCIV")


if __name__ == "__main__":
    unittest.main()
