#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-12-29 20:30:00
# 抖音二面 通过日志文件或标准输入的方式，读入一段文本，统计其中的英文单词出现的次数，并按照降序输出


def stat_words(content: str):
    if not content:
        return
    dic = dict()
    for word in content.split(" "):
        if not word:
            continue
        if word in dic:
            dic[word] += 1
        else:
            dic.setdefault(word, 1)
    dic_sorted = sorted(dic.items(), key=lambda kv: kv[1], reverse=True)
    for k, v in dic_sorted:
        print(k, v)


if __name__ == '__main__':
    my_content = input("please input some words: ")
    stat_words(content=my_content)


# 面试总结:
# 1、总体聊的很平平，面试官似乎不太感兴趣，有点像走过场
# 2、中途各种被打断，做的事情应该大家都熟，可能也没啥好问的
# 3、技术问题上，问了装饰器（回答上了），问了多线程和锁（直接说了没怎么用过）
# 4、出了上面这题，很简单了，竟然忘记了sorted的key怎么写，吐血... (LeetCode大概刷了100题，完全没用上)
# 5、最后问了觉得自己有什么缺点，感觉没答好，整场下来感觉有点紧张（可能因为面试周期拉太长了，外加最近阳了，压力比较大）
