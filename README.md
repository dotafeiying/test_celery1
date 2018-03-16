# test_celery1
django+vue.js前后端分离demo
## 技术栈：前端 vue+vuex+elementui+axios+webpack，后端 django+restframework

这是一个django与vue.js相结合的前后端分离项目的简单demo，为了节约时间，我采用网上找到的一个例子（具体请参考https://www.cnblogs.com/mysql-dba/p/6895190.html，这不是该项目要说的重点），在此基础上进行扩展。
vueAdmin-template文件夹存放前后端分离的前端文件。项目中的数据库配置以及跨域请求ip改为自己的ip

# 功能包括：
1、利用django restframe work提供接口给前端，包括token、用户信息以及其他需要进行前端展示的接口（需要对原有的auth_user表进行扩展，token表与用户信息表分开）。

2、django传统页面采用session登录，前后端分离项目采用token登录（即根据用户提供的用户名和密码等信息获取到token并保存到cookie，再根据token获取用户其他个人信息保存到vuex的store。这样就完成了用户的登录功能）

注意：ajax与axios发送post请求的区别，ajax默认发送post请求是application/x-www-form-urlencoded，而axios发送post请求是json，这样django后台是接受不到前端请求的，为了解决这个问题引入了jquery，jquery提供了$.param方法，非常方便，具体见代码。

