from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import BaseVersioning
from rest_framework.versioning import QueryParameterVersioning  #获取version的值
from rest_framework.versioning import URLPathVersioning #支持版本
from rest_framework.versioning import HostNameVersioning
from rest_framework.parsers import JSONParser  #解析器
from rest_framework import serializers
from app01 import models
class UsersSerializer(serializers.Serializer):
    name = serializers.CharField()  #字段名字
    age = serializers.CharField()
    hire_date=serializers.DateField()

class UserView(APIView):
    def get(self,request,*args,**kwargs):
        # 方式一实现
        # user_list = models.UserInfo.objects.values('name','pwd','group__mu','group__title')
        # print(type(user_list))
        # return Response(user_list)

        # 方式二之多对象
        # user_list = models.UserInfo.objects.all()  #直接这样查会报错，借助他提供的系列化
        # ser = UsersSerializer(instance=user_list,many=True) #可允许多个
        # # print(type(ser))  #<class 'rest_framework.serializers.ListSerializer'>
        # print(ser.data)  #返回的是一个有序字典

        #方式三之单对象
        user = models.Employee.objects.all()
        ser = UsersSerializer(instance=user,many=True)

        return Response(ser.data)
