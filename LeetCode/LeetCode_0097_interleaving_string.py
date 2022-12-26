#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-26 10:18:52

# 导入所需的依赖库
import unittest

# 题目编号: 97
# 题目名称: 交错字符串
# 题目难度: Medium

# 知识点: 字符串, 动态规划

# 题目详情:
"""
给定三个字符串&nbsp;s1、s2、s3，请你帮忙验证&nbsp;s3&nbsp;是否是由&nbsp;s1&nbsp;和&nbsp;s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：


	s = s1 + s2 + ... + sn
	t = t1 + t2 + ... + tm
	|n - m| &lt;= 1
	交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...


注意：a + b 意味着字符串 a 和 b 连接。

&nbsp;

示例 1：


输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true


示例 2：


输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false


示例 3：


输入：s1 = "", s2 = "", s3 = ""
输出：true


&nbsp;

提示：


	0 &lt;= s1.length, s2.length &lt;= 100
	0 &lt;= s3.length &lt;= 200
	s1、s2、和 s3 都由小写英文字母组成


&nbsp;

进阶：您能否仅使用 O(s2.length) 额外的内存空间来解决它?

"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        x, y, z = len(s1), len(s2), len(s3)

        if x + y != z:
            return False

        f = [[False] * (y + 1) for _ in range(x + 1)]

        f[0][0] = True

        for i in range(x + 1):
            for j in range(y + 1):
                p = i + j - 1
                if i > 0:
                    f[i][j] = f[i][j] | (f[i - 1][j] and s1[i-1] == s3[p])
                if j > 0:
                    f[i][j] = f[i][j] | (f[i][j - 1] and s2[j-1] == s3[p])

        return f[x][y]




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
