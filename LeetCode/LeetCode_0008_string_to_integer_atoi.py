#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-29 11:05:35

# 导入所需的依赖库
import unittest

# 题目编号: 8
# 题目名称: 字符串转换整数 (atoi)
# 题目难度: Medium

# 知识点: 字符串

# 题目详情:
"""
请你来实现一个&nbsp;myAtoi(string s)&nbsp;函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数&nbsp;myAtoi(string s) 的算法如下：


	读入字符串并丢弃无用的前导空格
	检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
	读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
	将前面步骤读入的这些数字转换为整数（即，"123" -&gt; 123， "0032" -&gt; 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
	如果整数数超过 32 位有符号整数范围 [−231,&nbsp; 231&nbsp;− 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231&nbsp;− 1 的整数应该被固定为 231&nbsp;− 1 。
	返回整数作为最终结果。


注意：


	本题中的空白字符只包括空格字符 ' ' 。
	除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。


&nbsp;

示例&nbsp;1：


输入：s = "42"
输出：42
解释：加粗的字符串为已经读入的字符，插入符号是当前读取的字符。
第 1 步："42"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："42"（读入 "42"）
           ^
解析得到整数 42 。
由于 "42" 在范围 [-231, 231 - 1] 内，最终结果为 42 。

示例&nbsp;2：


输入：s = "   -42"
输出：-42
解释：
第 1 步："   -42"（读入前导空格，但忽视掉）
            ^
第 2 步："   -42"（读入 '-' 字符，所以结果应该是负数）
             ^
第 3 步："   -42"（读入 "42"）
               ^
解析得到整数 -42 。
由于 "-42" 在范围 [-231, 231 - 1] 内，最终结果为 -42 。


示例&nbsp;3：


输入：s = "4193 with words"
输出：4193
解释：
第 1 步："4193 with words"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："4193 with words"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："4193 with words"（读入 "4193"；由于下一个字符不是一个数字，所以读入停止）
             ^
解析得到整数 4193 。
由于 "4193" 在范围 [-231, 231 - 1] 内，最终结果为 4193 。


&nbsp;

提示：


	0 &lt;= s.length &lt;= 200
	s 由英文字母（大写和小写）、数字（0-9）、' '、'+'、'-' 和 '.' 组成


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class DFA:

    INT_MAX = 2 ** 31 -1
    INT_MIN = -2 ** 31

    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def reset(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0

    def get_type(self, ch: str):
        if ch.isspace():
            return 0
        if ch in ['+', '-']:
            return 1
        if ch.isdigit():
            return 2
        return 3

    def get(self, ch):
        self.state = self.table[self.state][self.get_type(ch)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(ch)
            self.ans = min(self.ans, self.INT_MAX) if self.sign == 1 else min(self.ans, -self.INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if ch == '+' else -1


class Solution:

    def myAtoi(self, s: str) -> int:
        dfa = DFA()
        dfa.reset()
        for ch in s:
            dfa.get(ch)
        return dfa.sign * dfa.ans


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual(self.inst.myAtoi("42"), 42)

    def test_2(self):
        self.assertEqual(self.inst.myAtoi("-42"), -42)

    def test_3(self):
        self.assertEqual(self.inst.myAtoi("4193 with words"), 4193)


if __name__ == "__main__":
    unittest.main()
