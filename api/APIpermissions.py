# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
from rest_framework import permissions
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.authtoken.models import Token

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        """针对每一次请求的权限检查"""
        # print(request.user)
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # if not request.user.is_authenticated():
        #     return False

        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated()
        else:
            return request.user.is_staff

        # username=request.GET.get('username',None)
        # password = request.GET.get('password', None)
        #
        # user = auth.authenticate(username=username, password=password)
        # print(user)
        # if user:
        #     if request.method in permissions.SAFE_METHODS:
        #         return user
        #         # return request.user and request.user.is_authenticated()
        #     else:
        #         return user.is_staff
        # else:
        #     return False


    # def has_object_permission(self, request, view, obj):
    #     """针对数据库条目的权限检查，返回 True 表示允许"""
    #     # 允许访问只读方法
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #
    #     # 非安全方法需要检查用户是否是 owner
    #     return obj.owner == request.user
