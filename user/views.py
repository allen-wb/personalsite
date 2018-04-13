from django.http import HttpResponse
from user.models import User
import json


def index(request):
    return HttpResponse("Hello, world. You're at the user index.")


def login(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    user_name = body['username']
    password = body['password']
    #
    try:
        user = User.objects.get(user_name=user_name, password=password)
    except User.DoesNotExist:
        res = {'code': 100, 'message': '用户名密码错误'}
        return HttpResponse(json.dumps(res), content_type='application/json')
    # session的使用
    request.session['name'] = user_name
    request.session['user_id'] = user.user_id
    request.session.set_expiry(None)
    res = {'code': 200, 'message': '登录成功', 'name': user_name}
    return HttpResponse(json.dumps(res), content_type='application/json')


def update_password(request):
    data = json.loads(request.body.decode('utf-8'))
    user_name = data.get('user_name', None)
    old_password = data.get('old_password', None)
    new_password = data.get('new_password', None)
    repeat_password = data.get('repeat_password', None)
    if (not user_name) or (not old_password) or (not new_password) or (not repeat_password):
        res = {'code': 100, 'message': '参数不能为空'}
    if len(new_password.strip()) < 6:
        res = {'code': 100, 'message': '新密码长度必须在6位-16位之间'}
    if new_password != repeat_password:
        res = {'code': 100, 'message': '密码不一致'}
    try:
        user = User.objects.get(user_name=user_name, password=old_password)
        if user:
            user.password = new_password.strip()
            user.save(update_fields=user.password)
            res = {'code': 200, 'message': '修改成功'}
    except User.DoesNotExist:
        res = {'code': 100, 'message': '原密码错误'}

    return HttpResponse(json.dumps(res), content_type='application/json')


def get_user_by_name(request):
    data = json.loads(request.body.decode('utf-8'))
    user_name = data.get('user_name', None)
    if not user_name:
        try:
            user = User.objects.get(user_name=user_name)
            res = {'code': 200, 'message': user}
        except User.DoesNotExist:
            res = {'code': 100, 'message': '查询不到该用户信息,请重新登录'}
    else:
        res = {'code': 100, 'message': '缺少参数'}
    return HttpResponse(json.dumps(res), content_type='application/json')


def update_personal_info(request):
    data = json.loads(request.body.decode('utf-8'))
    pass
