"""test_celery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from rest_framework import routers
# from .views import AddViewSet,userlogin,userinfo
from . import views
from rest_framework.authtoken.views import obtain_auth_token



router = routers.DefaultRouter()
router.register(r'add', views.AddViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # 验证登录使用
    url(r'auth', include('rest_framework.urls')),
    # url(r'^api-token-auth/', obtain_auth_token), # 获取token
    url(r'^user/login', views.userlogin), # 获取token
    url(r'^user/info', views.userinfo), # 获取用户信息
    url(r'^user/logout', views.userlogout), # 登出
    url(r'^test/$', views.GetMessageView.as_view()),
    url(r'table1/$', views.AddList.as_view())

]
