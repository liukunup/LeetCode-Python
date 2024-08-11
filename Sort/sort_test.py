#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2024-08-11 22:11:10

import unittest
import random
import copy
import time
from typing import List
from functools import wraps


def timeit(func):
    """
    用于统计函数执行耗时的注解
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    return wrapper


# 请完成以下开发代码(如不符合语法要求,自行修改即可)
class Solution:

    @timeit
    @staticmethod
    def bubble_sort(nums: List[int]) -> List[int]:
        """
        冒泡排序
        时间复杂度: O(N^2) 最坏情况下，需要进行n(n-1)/2次比较和交换操作。
        空间复杂度: O(1)
        :param nums: 待排序的数组
        :return: 已排序的数组
        """
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

    @staticmethod
    def quick_sort(nums: List[int]) -> List[int]:
        """
        快速排序
        时间复杂度: 在平均情况下是O(NlogN)，但在最坏情况下可能达到O(N^2)。
        空间复杂度: 理想情况下为O(logN)，但在最坏情况下可能达到O(n)。
        :param nums: 待排序的数组
        :return: 已排序的数组
        """
        if len(nums) <= 1:
            return nums

        pivot = nums[len(nums) // 2]
        left   = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right  = [x for x in nums if x > pivot]

        return Solution.quick_sort(left) + middle + Solution.quick_sort(right)


# 请完成以下测试代码
class SolutionTest(unittest.TestCase):

    def setUp(self):
        # 生成 1 到 N 的乱序数字列表
        self.n = 10000
        self.nums = list(range(1, self.n + 1))
        random.shuffle(self.nums)

    def tearDown(self):
        pass

    # 请设计一些测试用例来验证
    def test_bubble_sort(self):
        copied = copy.deepcopy(self.nums)
        result = Solution.bubble_sort(copied)
        print(result[:10])

    def test_quick_sort(self):

        @timeit
        def f_quick_sort(var):
            return Solution.quick_sort(var)

        copied = copy.deepcopy(self.nums)
        result = f_quick_sort(copied)
        print(result[:10])


if __name__ == "__main__":
    unittest.main()
