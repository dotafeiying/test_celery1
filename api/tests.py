# -*- coding: utf-8 -*-
import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','test_celery.settings')
django.setup()

from test_celery.models import Add,LayuiDemo1
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate

data=LayuiDemo1.objects.using('db1').all()
print(data)

# blog=BlogComment.objects.get(id=37)
# print(blog)
# article_list=Article.objects.all()
# print(article_list)
# for article in article_list:
#     article.comments=len(article.blogcomment_set.all())
# print(article_list)
# print([(x.title,x.comments) for x in article_list])

# article=Article.objects.filter(status='p').filter(category__slug='szyf',type__slug='jz').get(pk=1053)
# print(article.category.slug)
# type_list = AboutType.objects.all().order_by('-created_time')
# article_type_list = []
# for type in type_list:
#     article_type_list.append(About.objects.filter(category=type.name).order_by('-created_time')[0:7])

# token='fb961aa490da395e13f3b21bd3e0328bcbbf2592'
token='db3e7f073459b16772a511f3b87e2ca1de36b4d8'
# b=User.objects.filter(username="xulu")
# a=Token.objects.filter(key=token)
# # role=Group.objects.filter(id=a[0].user.group_id)
# print(a[0].user)
# # print(Group.objects.filter(user_set=a[0].user))
# print(a[0].user.get_all_permissions())
# # print(role)
# print(a.values())
# userid1=Token.objects.filter(key=token).select_related('user')[0].user_id
# print(userid)
# group = Group.objects.filter(user=userid)[0]
# # users = group.user_set.all()
# print(group)
# userid1=Token.objects.filter(key=token)[0].user.username

# userid1=User.objects.filter(auth_token=token).prefetch_related('groups').first()
# print(userid1.username)
# print(type(userid1))
# print(userid1.groups.first())

# def main():
#     columns_urls = [
#         ('体育新闻', 'sports'),
#         ('社会新闻', 'society'),
#         ('科技新闻', 'tech'),
#     ]
#
#
#     # 创建 10 篇新闻
#     import random
#     for i in range(1, 1100):
#         article = Add.objects.get_or_create(
#             task_id=random.randint(345325235,3535466436),
#             first=random.randint(1,10000),
#             second=random.randint(1,10000),
#             log_date="2018-01-15T11:57:43.343558",
#         )[0]
#
#
# if __name__ == '__main__':
#     main()
#     print("Done!")

