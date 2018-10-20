# coding:utf-8
# from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.db import connection
# Django中对于基于函数的视图我们可以 @csrf_exempt 注解来标识一个视图可以被跨域访问
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add(request):
    print('''request=======>%s'''%(request))
    if request.method == 'GET':
        SQL_str = "select * from user_info"
        # 游标
        cursor = connection.cursor()
        # 执行sql语句
        cursor.execute(SQL_str)
        # 获取返回值
        result = cursor.fetchall()
        # 关闭游标
        cursor.close()
        # if answer == None :
        return HttpResponse(result)

    elif request.method == 'POST':
        SQL_str = "select * from user_info"
        # 游标
        cursor = connection.cursor()
        # 执行sql语句
        cursor.execute(SQL_str)
        # 获取返回值
        result = cursor.fetchall()
        # 关闭游标
        cursor.close()
        # if answer == None :
        return HttpResponse(result)

    elif request.method == 'DELETE':
        return HttpResponse('DELETE')
    elif request.method == 'PUT':
        return HttpResponse('PUT')
    else:
        return HttpResponse('error')