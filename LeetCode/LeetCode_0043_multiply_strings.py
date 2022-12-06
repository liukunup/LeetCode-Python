#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-06 16:26:22

# 导入所需的依赖库
import unittest

# 题目编号: 43
# 题目名称: 字符串相乘
# 题目难度: Medium

# 知识点: 数学, 字符串, 模拟

# 题目详情:
"""
给定两个以字符串形式表示的非负整数&nbsp;num1&nbsp;和&nbsp;num2，返回&nbsp;num1&nbsp;和&nbsp;num2&nbsp;的乘积，它们的乘积也表示为字符串形式。

注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。

&nbsp;

示例 1:


输入: num1 = "2", num2 = "3"
输出: "6"

示例&nbsp;2:


输入: num1 = "123", num2 = "456"
输出: "56088"

&nbsp;

提示：


	1 &lt;= num1.length, num2.length &lt;= 200
	num1&nbsp;和 num2&nbsp;只能由数字组成。
	num1&nbsp;和 num2&nbsp;都不包含任何前导零，除了数字0本身。


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        # 任一为 0
        if num1 == '0' or num2 == '0':
            return '0'

        # 9 * 9 = 81
        # 99 * 99 < 100 * 100 < 10000 4位数字
        # 结论: 乘积的位数不会超过两个乘树的位数和
        nums = [0] * (len(num1) + len(num2))

        # 优化乘法
        for i in range(len(num1) - 1, -1, -1):
            num_i = int(num1[i])
            for j in range(len(num2) - 1, -1, -1):
                num_j = int(num2[j])
                # 两个数字相乘 最多只会是两位数 比如 9*9=81
                #
                tmp_sum = nums[i + j + 1] + num_i * num_j
                nums[i + j + 1] = tmp_sum % 10
                nums[i + j] += tmp_sum // 10

        # 注意首位是否为0
        ans = []
        for i, val in enumerate(nums):
            if i == 0 and val == 0:
                continue
            ans.append(f'{val}')

        return ''.join(ans)


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_xxx(self):
        self.assertEqual('9801', self.inst.multiply("99", "99"))


if __name__ == "__main__":
    unittest.main()
