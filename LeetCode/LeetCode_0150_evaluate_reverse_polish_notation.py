#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2023-03-04 10:30:58

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 150
# 题目名称: 逆波兰表达式求值
# 题目难度: Medium

# 知识点: 栈, 数组, 数学

# 题目详情:
"""
给你一个字符串数组 tokens ，表示一个根据&nbsp;逆波兰表示法 表示的算术表达式。

请你计算该表达式。返回一个表示表达式值的整数。

注意：


	有效的算符为 '+'、'-'、'*' 和 '/' 。
	每个操作数（运算对象）都可以是一个整数或者另一个表达式。
	两个整数之间的除法总是 向零截断 。
	表达式中不含除零运算。
	输入是一个根据逆波兰表示法表示的算术表达式。
	答案及所有中间计算结果可以用 32 位 整数表示。


&nbsp;

示例&nbsp;1：


输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9


示例&nbsp;2：


输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6


示例&nbsp;3：


输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

&nbsp;

提示：


	1 &lt;= tokens.length &lt;= 104
	tokens[i]&nbsp;是一个算符（"+"、"-"、"*" 或 "/"），或是在范围 [-200, 200] 内的一个整数


&nbsp;

逆波兰表达式：

逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。


	平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
	该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。


逆波兰表达式主要有以下两个优点：


	去掉括号后表达式无歧义，上式即便写成 1 2 + 3 4 + * 也可以依据次序计算出正确结果。
	适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中


"""

# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_to_binary_fn = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),  # 需要注意 python 中负数除法的表现与题目不一致
        }

        stack = list()
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            finally:
                stack.append(num)

        return stack[0]


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual(9, self.inst.evalRPN(["2","1","+","3","*"]))
        self.assertEqual(6, self.inst.evalRPN(["4","13","5","/","+"]))
        self.assertEqual(22, self.inst.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


if __name__ == "__main__":
    unittest.main()
