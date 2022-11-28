#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-28 23:00:20

# 导入所需的依赖库
import unittest
from typing import List

# 题目编号: 26
# 题目名称: 删除有序数组中的重复项
# 题目难度: Easy

# 知识点: 数组, 双指针

# 题目详情:
"""
给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。

由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。更规范地说，如果在删除重复项之后有 k 个元素，那么&nbsp;nums&nbsp;的前 k 个元素应该保存最终结果。

将最终结果插入&nbsp;nums 的前 k 个位置后返回 k 。

不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

判题标准:

系统会用下面的代码来测试你的题解:


int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i &lt; k; i++) {
    assert nums[i] == expectedNums[i];
}

如果所有断言都通过，那么您的题解将被 通过。

&nbsp;

示例 1：


输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。


示例 2：


输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。


&nbsp;

提示：


	1 &lt;= nums.length &lt;= 3 * 104
	-104 &lt;= nums[i] &lt;= 104
	nums 已按 升序 排列


"""


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1

    def removeDuplicates_v2(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n
        return self.processK(nums, k=1, max_val=nums[n-1])

    def processK(self, nums: List[int], k: int, max_val: int) -> int:
        n = len(nums)
        j = 0
        for i in range(n):
            if j < k or nums[i] != nums[j - k]:
                nums[j] = nums[i]
                j += 1
            if j - k >= 0 and nums[j - k] == max_val: break
        return j


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.inst = Solution()

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_1(self):
        self.assertEqual(self.inst.removeDuplicates_v2(nums=[1, 1, 2]), 2)

    def test_2(self):
        self.assertEqual(self.inst.removeDuplicates_v2(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)


if __name__ == "__main__":
    unittest.main()
