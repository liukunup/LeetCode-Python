#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:    LiuKun
# timestamp: 2022-11-11 12:00:00
# brief:     LeetCode Crawler

import typing as t
import re
import requests
import json
import datetime
import click


class LeetCodeCrawler:
    """ LeetCode爬虫工具 """

    def __init__(self, debug: bool = False):
        self.__debug = debug

    def execute(self, question_url: t.Text):
        """
        执行爬取动作
        :param question_url: 题目链接
        :return: 不涉及
        """
        if question_url:
            self.__gen(self.__req(question_url=question_url, debug=self.__debug))
        else:
            print("请输入待拉取的题目链接!")

    @staticmethod
    def __req(question_url: t.Text, debug: bool = False):
        """
        从LeetCode网站拉取题目
        :param question_url: 题目链接
        :param debug:        调试开关（默认关闭）
        :return: 题目信息（JSON）
        """
        try:
            # 通过正则表达式提取题目名
            param = re.search(r"^https://leetcode.cn/problems/(?P<question>[A-Za-z0-9\-]+)/$", question_url)
            question = param.group("question")
            # 读取题目查询GraphQL语句
            graphql = None
            with open("QuestionData.graphql", "r", encoding="UTF-8") as f:
                graphql = f.read()
                if debug:
                    # 打印查询语句
                    print(graphql)
            # 通过LeetCode接口获取题目信息
            graphql_url = "https://leetcode.cn/graphql/"
            payload = {
                "operationName": "questionData",
                "variables": {"titleSlug": question},
                "query": graphql,
            }
            headers = {"Content-Type": "application/json;charset=UTF-8"}
            response = requests.post(graphql_url, headers=headers, data=json.dumps(payload))
            obj = response.json()
            if debug:
                # 打印查询结果
                print(json.dumps(obj, sort_keys=True, indent=4, separators=(", ", ": "), ensure_ascii=False))
            return obj
        except Exception as e:
            print(question_url)
            print(e)
        return None

    @staticmethod
    def __gen(question_obj, lang="Python3", debug=False):
        """
        将拉取的题目发布成代码模板文件
        :param question_obj: 题目链接
        :param lang:         编程语言
        :param debug:        调试开关
        :return: 不涉及
        """
        try:
            # 读取题目模板
            question_template = None
            with open("Python3.template", "r", encoding="UTF-8") as f:
                question_template = f.read()
                if debug:
                    # 打印查询语句
                    print(question_template)
            # 写入代码模板
            question = question_obj["data"]["question"]
            question_id = question["questionId"]  # 题目编号
            title_slug = question["titleSlug"]  # 题目名称
            with open(f"LeetCode_{question_id.zfill(4)}_{title_slug.replace('-', '_')}.py", "w", encoding="UTF-8") as f:
                # 配置模板里所需的参数
                args = list()
                # 作者+时间戳
                args.extend(["LiuKun", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
                # 题目编号、名称、难度
                args.append(question_id)
                args.append(question["translatedTitle"])  #
                args.append(question["difficulty"])  #
                # 题目知识点
                tags = list()
                for item in question["topicTags"]:
                    tags.append(item["translatedName"])
                args.append(", ".join(tags))
                # 题目内容
                translated_content = question["translatedContent"]
                pattern = re.compile(r"<[^>]*>", re.S)
                translated_content_pure = pattern.sub("", translated_content)
                args.append(translated_content_pure)
                # 题目代码模板
                code_snippets = question["codeSnippets"]
                for item in code_snippets:
                    if item["lang"] != lang:
                        continue
                    code = item["code"]
                    args.append(code)
                # 写入到文件
                f.write(question_template % tuple(args))
        except Exception as e:
            print(e)


@click.group()
def cli():
    pass


@cli.command()
@click.option("--url", help="The LeetCode question url.")
def crawler(url):
    """ LeetCode 题目爬取&生成代码 """
    if url:
        inst = LeetCodeCrawler()
        inst.execute(url)
    else:
        print("请输入待拉取的题目链接")


if __name__ == '__main__':
    cli()
