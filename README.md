

# erp

> 一个更新缓慢的个人博客后台

## Build Setup

``` bash
# 基于pgsql
    # 请安装依赖 psycopg2
    # 为了让psycopg2兼容python3 下载二进制的psycopg2包
    pip install -U pip
    pip install psycopg2

    # 如果失败的话
    sudo apt install pip3
    pip3 install psycopg2
    pip3 install psycopg2-binary


# 支持 localhost/127.0.0.1/本地IP地址  打开的食用方式 端口号看个人爱好
python manage.py runserver 0.0.0.0:3000

```

## 前后端分离的 django project
> 前端代码传送门 [前端github地址](https://github.com/liaowentuan/index).