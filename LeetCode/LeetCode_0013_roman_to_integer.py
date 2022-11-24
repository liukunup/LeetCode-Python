#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-24 23:51:06

# 导入所需的依赖库
import unittest

# 题目编号: 13
# 题目名称: 罗马数字转整数
# 题目难度: Easy

# 知识点: 哈希表, 数学, 字符串

# 题目详情:
"""
罗马数字包含以下七种字符:&nbsp;I，&nbsp;V，&nbsp;X，&nbsp;L，C，D&nbsp;和&nbsp;M。


字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做&nbsp;II&nbsp;，即为两个并列的 1 。12 写做&nbsp;XII&nbsp;，即为&nbsp;X&nbsp;+&nbsp;II&nbsp;。 27 写做&nbsp;&nbsp;XXVII, 即为&nbsp;XX&nbsp;+&nbsp;V&nbsp;+&nbsp;II&nbsp;。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做&nbsp;IIII，而是&nbsp;IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为&nbsp;IX。这个特殊的规则只适用于以下六种情况：


	I&nbsp;可以放在&nbsp;V&nbsp;(5) 和&nbsp;X&nbsp;(10) 的左边，来表示 4 和 9。
	X&nbsp;可以放在&nbsp;L&nbsp;(50) 和&nbsp;C&nbsp;(100) 的左边，来表示 40 和&nbsp;90。&nbsp;
	C&nbsp;可以放在&nbsp;D&nbsp;(500) 和&nbsp;M&nbsp;(1000) 的左边，来表示&nbsp;400 和&nbsp;900。


给定一个罗马数字，将其转换成整数。

&nbsp;

示例&nbsp;1:


输入:&nbsp;s = "III"
输出: 3

示例&nbsp;2:


输入:&nbsp;s = "IV"
输出: 4

示例&nbsp;3:


输入:&nbsp;s = "IX"
输出: 9

示例&nbsp;4:


输入:&nbsp;s = "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.


示例&nbsp;5:


输入:&nbsp;s = "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

&nbsp;

提示：


	1 &lt;= s.length &lt;= 15
	s 仅含字符 ('I', 'V', 'X', 'L', 'C', 'D', 'M')
	题目数据保证 s 是一个有效的罗马数字，且表示整数在范围 [1, 3999] 内
	题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
	IL 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
	关于罗马数字的详尽书写规则，可以参考 罗马数字 - Mathematics 。


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            value = self.SYMBOL_VALUES.get(ch)
            if i < n - 1 and value < self.SYMBOL_VALUES.get(s[i + 1]):
                ans -= value
            else:
                ans += value
        return ans


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual(self.inst.romanToInt("III"), 3)

    def test_2(self):
        self.assertEqual(self.inst.romanToInt("IV"), 4)

    def test_3(self):
        self.assertEqual(self.inst.romanToInt("IX"), 9)

    def test_4(self):
        self.assertEqual(self.inst.romanToInt("LVIII"), 58)

    def test_5(self):
        self.assertEqual(self.inst.romanToInt("MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()
