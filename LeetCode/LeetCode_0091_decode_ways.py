#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-16 18:46:38

# 导入所需的依赖库
import unittest

# 题目编号: 91
# 题目名称: 解码方法
# 题目难度: Medium

# 知识点: 字符串, 动态规划

# 题目详情:
"""
一条包含字母&nbsp;A-Z 的消息通过以下映射进行了 编码 ：


'A' -&gt; "1"
'B' -&gt; "2"
...
'Z' -&gt; "26"

要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：


	"AAJF" ，将消息分组为 (1 1 10 6)
	"KJF" ，将消息分组为 (11 10 6)


注意，消息不能分组为&nbsp; (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。

给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。

题目数据保证答案肯定是一个 32 位 的整数。

&nbsp;

示例 1：


输入：s = "12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。


示例 2：


输入：s = "226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。


示例 3：


输入：s = "06"
输出：0
解释："06" 无法映射到 "F" ，因为存在前导零（"6" 和 "06" 并不等价）。


&nbsp;

提示：


	1 &lt;= s.length &lt;= 100
	s 只包含数字，并且可能包含前导零。


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                f[i] += f[i - 2]
        return f[n]


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(2, self.inst.numDecodings(s="11106"))
        self.assertEqual(3, self.inst.numDecodings(s="226"))
        self.assertEqual(2, self.inst.numDecodings(s="12"))
        self.assertEqual(0, self.inst.numDecodings(s="06"))
        self.assertEqual(1, self.inst.numDecodings(s="2101"))
        self.assertEqual(1, self.inst.numDecodings(s="27"))
        self.assertEqual(2, self.inst.numDecodings(s="12"))


if __name__ == "__main__":
    unittest.main()
