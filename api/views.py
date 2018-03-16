from django.shortcuts import render
import json
from collections import OrderedDict
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,Group
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from rest_framework import viewsets, filters
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import parsers, renderers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, detail_route,list_route
from rest_framework.renderers import JSONRenderer
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status

from test_celery.models import Add
from .serializer import AddSerializer
from . import APIpermissions

class AddList(APIView):
    def get(self, request, format=None):
        response = OrderedDict()
        snippets = Add.objects.all()
        serializer = AddSerializer(snippets, many=True, context={'request': request})
        response['code'] = 20000
        response['data'] = serializer.data
        return Response(response)
        # return Response(serializer.data)
    def post(self, request, format=None):
        serializer = AddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddViewSet(viewsets.ModelViewSet):
    queryset = Add.objects.all()
    serializer_class = AddSerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication,TokenAuthentication)
    permission_classes = (permissions.IsAdminUser,)
    # permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (APIpermissions.IsOwnerOrReadOnly,)

    #自定义方法plaintext 访问路径/api/add/copy/
    @list_route(url_path='copy')
    def plaintext(self, request, *args, **kwargs):
        """自定义 Api 方法"""
        response=OrderedDict()
        model=self.get_queryset()
        # serializer = AddSerializer(model, many=True)
        # print(serializer.data)
        # response['data']=serializer.data
        response['code']=20000
        response['data']=model.values()
        # return Response(serializer.data)
        # return JsonResponse(response)
        # return JsonResponse(json.loads(serializers.serialize("json", model)),safe=False)
        print(response)
        return Response(response)

class GetMessageView(APIView):
    # get 请求
    def get(self, request):
        # 获取参数数据
        get = request.GET
        # 获取参数 a
        a = get.get('a')
        print(a)
        # 返回信息
        d = {
            'status': 1,
            'message': 'success',
            }
        # d=Add.objects.all()
        # serializer = AddSerializer(d, many=True)
        # d=JSONRenderer().render(serializer.data)
        from rest_framework.response import Response
        return Response(d)

@csrf_exempt
def userlogin(request):
    response = {}
    if request.method=='POST':
        # print(request.body)
        data=json.loads(request.body.decode('utf8'))
        # username=request.POST.get('username')
        # print(username)
        # print(data)
        username=data.get('username')
        password=data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            # print(token.key)
            response['code']=20000
            response['data']={'token':token.key}
        else:
            response['code'] = 50000
            response['data'] = '登陆账号不对'
        print(response)
        return JsonResponse(response)

def userinfo(request):
    if request.method=='GET':
        response=OrderedDict()
        token=request.GET.get('token')
        if token:
            user = User.objects.filter(auth_token=token).prefetch_related('groups').first()
            if user:
                username=user.username
                role=user.groups.first()
                if role:
                    role=role.name
                else:
                    role="staff"
                response['code'] = 20000
                response['data'] = {"roles":[role],"role":[role],"name":username,"avatar":"https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"}
            else:
                response['code'] = 50000
                response['data'] = '用户不存在'
        else:
            response['code']=50000
            response['data']='登录失败'
        print(response)
        return JsonResponse(response)

@csrf_exempt
def userlogout(request):
    if request.method=='POST':
        response=OrderedDict()
        response['code']=20000
        response['data']='success'
        print(response)
        return JsonResponse(response)


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})