#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-14 17:56:51

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 93
# 题目名称: 复原 IP 地址
# 题目难度: Medium

# 知识点: 字符串, 回溯

# 题目详情:
"""
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。


	例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。


给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入&nbsp;'.' 来形成。你 不能&nbsp;重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

&nbsp;

示例 1：


输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]


示例 2：


输入：s = "0000"
输出：["0.0.0.0"]


示例 3：


输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


&nbsp;

提示：


	1 &lt;= s.length &lt;= 20
	s 仅由数字组成


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        s_len = len(s)

        def dfs(pos, path):
            #
            if len(path) > 4:
                return
            # 字符串结束
            if pos == s_len and len(path) == 4:
                res.append('.'.join(path))
                return
            # 遍历
            for i in range(1, 4):  # 最少1位 最多3位
                #
                ss = s[pos: min(pos + i, s_len)]
                #
                if not ss:
                    continue
                if i > 1 and ss.startswith('0'):
                    continue
                if int(ss) > 255:
                    continue
                #
                dfs(pos + i, path + [ss])

        # 存结果
        res = list()
        dfs(0, [])

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
        self.assertEqual(["255.255.11.135", "255.255.111.35"], self.inst.restoreIpAddresses(s="25525511135"))


if __name__ == "__main__":
    unittest.main()
