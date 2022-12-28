#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-26 17:35:03

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 68
# 题目名称: 文本左右对齐
# 题目难度: Hard

# 知识点: 数组, 字符串, 模拟

# 题目详情:
"""
给定一个单词数组&nbsp;words 和一个长度&nbsp;maxWidth&nbsp;，重新排版单词，使其成为每行恰好有&nbsp;maxWidth&nbsp;个字符，且左右两端对齐的文本。

你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格&nbsp;' '&nbsp;填充，使得每行恰好有 maxWidth&nbsp;个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

注意:


	单词是指由非空格字符组成的字符序列。
	每个单词的长度大于 0，小于等于&nbsp;maxWidth。
	输入单词数组 words&nbsp;至少包含一个单词。


&nbsp;

示例 1:


输入: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
输出:
[
&nbsp; &nbsp;"This &nbsp; &nbsp;is &nbsp; &nbsp;an",
&nbsp; &nbsp;"example &nbsp;of text",
&nbsp; &nbsp;"justification. &nbsp;"
]


示例&nbsp;2:


输入:words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
输出:
[
&nbsp; "What &nbsp; must &nbsp; be",
&nbsp; "acknowledgment &nbsp;",
&nbsp; "shall be &nbsp; &nbsp; &nbsp; &nbsp;"
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
&nbsp;    因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。


示例&nbsp;3:


输入:words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]，maxWidth = 20
输出:
[
&nbsp; "Science &nbsp;is &nbsp;what we",
  "understand &nbsp; &nbsp; &nbsp;well",
&nbsp; "enough to explain to",
&nbsp; "a &nbsp;computer. &nbsp;Art is",
&nbsp; "everything &nbsp;else &nbsp;we",
&nbsp; "do &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"
]


&nbsp;

提示:


	1 &lt;= words.length &lt;= 300
	1 &lt;= words[i].length &lt;= 20
	words[i]&nbsp;由小写英文字母和符号组成
	1 &lt;= maxWidth &lt;= 100
	words[i].length &lt;= maxWidth


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    @staticmethod
    def blank(n: int) -> str:
        return " " * n

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        right, n = 0, len(words)

        while True:
            left = right
            sumLen = 0

            while right < n and sumLen + len(words[right]) + right - left <= maxWidth:
                sumLen += len(words[right])
                right += 1

            if right == n:
                s = " ".join(words[left:])
                ans.append(s + self.blank(maxWidth - len(s)))
                break

            numWords = right - left
            numSpaces = maxWidth - sumLen

            if numWords == 1:
                ans.append(words[left] + self.blank(numSpaces))
                continue

            avgSpaces = numSpaces // (numWords - 1)
            extraSpaces = numSpaces % (numWords - 1)
            s1 = self.blank(avgSpaces + 1).join(words[left:left + extraSpaces + 1])
            s2 = self.blank(avgSpaces).join(words[left + extraSpaces + 1:right])
            ans.append(s1 + self.blank(avgSpaces) + s2)

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
        self.assertEqual(0, -1)


if __name__ == "__main__":
    unittest.main()
