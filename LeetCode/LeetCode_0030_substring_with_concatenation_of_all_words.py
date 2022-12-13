#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-09 11:41:19

# 导入所需的依赖库
from collections import Counter
import unittest
from typing import List

# 题目编号: 30
# 题目名称: 串联所有单词的子串
# 题目难度: Hard

# 知识点: 哈希表, 字符串, 滑动窗口

# 题目详情:
"""
给定一个字符串&nbsp;s&nbsp;和一个字符串数组&nbsp;words。&nbsp;words&nbsp;中所有字符串 长度相同。

&nbsp;s&nbsp;中的 串联子串 是指一个包含&nbsp;&nbsp;words&nbsp;中所有字符串以任意顺序排列连接起来的子串。


	例如，如果&nbsp;words = ["ab","cd","ef"]， 那么&nbsp;"abcdef"，&nbsp;"abefcd"，"cdabef"，&nbsp;"cdefab"，"efabcd"， 和&nbsp;"efcdab" 都是串联子串。&nbsp;"acdbef" 不是串联子串，因为他不是任何&nbsp;words&nbsp;排列的连接。


返回所有串联字串在&nbsp;s&nbsp;中的开始索引。你可以以 任意顺序 返回答案。

&nbsp;

示例 1：


输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
输出顺序无关紧要。返回 [9,0] 也是可以的。


示例 2：


输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]
解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
所以我们返回一个空数组。


示例 3：


输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]
解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。

&nbsp;

提示：


	1 &lt;= s.length &lt;= 104
	1 &lt;= words.length &lt;= 5000
	1 &lt;= words[i].length &lt;= 30
	words[i]&nbsp;和&nbsp;s 由小写英文字母组成


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        res = []

        # words长度 单个词长度 原串长度
        ws_len, w_len, s_len = len(words), len(words[0]), len(s)

        # 移位尝试
        for i in range(w_len):

            # 尾部对齐时退出
            if i + ws_len * w_len > s_len:
                break

            differ = Counter()
            # 切分原串
            for j in range(ws_len):
                word = s[i + j * w_len: i + (j + 1) * w_len]
                differ[word] += 1
            # 对比模式串
            for word in words:
                differ[word] -= 1
                if differ[word] == 0:
                    del differ[word]
            # 从左往右 滑动
            for start in range(i, s_len - ws_len * w_len + 1, w_len):
                # 第一个窗口已经在上面处理了
                if start != i:
                    # 右边进
                    word = s[start + (ws_len - 1) * w_len: start + ws_len * w_len]
                    differ[word] += 1
                    if differ[word] == 0:
                        del differ[word]
                    # 左边出
                    word = s[start - w_len: start]
                    differ[word] -= 1
                    if differ[word] == 0:
                        del differ[word]
                # 恰好
                if len(differ) == 0:
                    res.append(start)

        return res

    def findSubstring_v2(self, s: str, words: List[str]) -> List[int]:
        # 简单明了
        s_len, w_str_len, w_len = len(s), len(words), len(words[0])
        w_ch_len = w_str_len * w_len

        return [
            i for i in range(s_len - w_ch_len + 1)
            if Counter(
                s[j: j + w_len] for j in range(i, i + w_ch_len, w_len)
            ) == Counter(words)
        ]


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual([0, 9], self.inst.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))


if __name__ == "__main__":
    unittest.main()
