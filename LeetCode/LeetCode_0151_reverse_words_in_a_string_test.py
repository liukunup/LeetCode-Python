#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2025-08-28 23:31:10

# 导入所需的依赖库
import unittest
from typing import Optional, List

# 题目编号: 151
# 题目名称: 反转字符串中的单词
# 题目难度: Medium

# 知识点: 双指针, 字符串

# 题目详情:
"""
给你一个字符串 s ，请你反转字符串中 单词 的顺序。

单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。

注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

&nbsp;

示例 1：


输入：s = "the sky is blue"
输出："blue is sky the"


示例 2：


输入：s = " &nbsp;hello world &nbsp;"
输出："world hello"
解释：反转后的字符串中不能存在前导空格和尾随空格。


示例 3：


输入：s = "a good &nbsp; example"
输出："example good a"
解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。


&nbsp;

提示：


	1 &lt;= s.length &lt;= 104
	s 包含英文大小写字母、数字和空格 ' '
	s 中 至少存在一个 单词





&nbsp;

进阶：如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用&nbsp;O(1) 额外空间复杂度的 原地 解法。

"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])
    
    def reverseWords_v2(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    def reverseWords_v3(self, s: str) -> str:
        ans = ''
        right = len(s) - 1
        # 去除右边空格
        while right > 0 and s[right] == ' ':
            right -= 1
        left = right
        # 找最后一个单词的左边界
        while left >= 0:
            while left >= 0 and s[left] != ' ':
                left -= 1
            ans += s[left+1:right+1] + ' '
            # 接着找下一个右边界
            right = left
            while right >=0 and s[right] == ' ':
                right -= 1
            left = right
        # 去除最后一个空格
        return ans[:-1]


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual(self.inst.reverseWords_v3(s = "the sky is blue"), "blue is sky the")


if __name__ == "__main__":
    unittest.main()
