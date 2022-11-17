# LeetCode-Python 刷题笔记

建议安装`Jupyter Notebook`作为刷题工具，在没有代码提示的情况下，更好的提升自身水平。

## 安装开发环境

* Jupyter镜像 [DockerHub](https://hub.docker.com/u/jupyter)

#### 镜像选择

![images](https://jupyter-docker-stacks.readthedocs.io/en/latest/_images/inherit.svg)

#### 镜像拉取

``` shell
docker pull jupyter/minimal-notebook:latest
```

#### 镜像运行

``` shell
docker run -d \
  -p 8888:8888 \
  -e JUPYTER_ENABLE_LAB=yes \
  -e GRANT_SUDO=yes \
  --restart=always \
  --name=minimal-notebook \
  jupyter/minimal-notebook:latest start-notebook.sh \
  --NotebookApp.password='sha1:a7c0702d28e9:8a8868c5d4ea33af70e04c634487402b3997f40c'
```

> 哈希密码生成方法

``` python
# 运行代码，按提示填写即可
from notebook.auth import passwd
passwd()
```

#### 登陆体验

* 浏览器打开 http://your-server-ip:8888/
* 在命令行窗口输入"docker ps"查找刚刚创建的容器实例
* 通过命令行"docker logs [容器id]"查看日志, 找到token用于登陆
* enjoy >_<

## 下载代码框架

> 克隆代码库

``` shell
git clone https://github.com/liukunup/LeetCode-Python.git
```

> 记得安装依赖库哦

``` shell
pip install -r requirements.txt
```


## 拉取题目开刷吧～

* 命令行方式

``` shell
python pull.py crawler --url=https://leetcode.cn/problems/two-sum/
```

* 笔记本方式

  - 打开`pull.ipynb`文件
  - 修改`url`链接
  - 挨个代码块执行
