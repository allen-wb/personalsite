from django.http import HttpResponse
from django.core import serializers
from menu.models import Menu
import json
import logging
import time

logger = logging.getLogger(__name__)


# Create your views here.
class MenuVO:
    def __init__(self, menu):
        self.menu_name = menu.menu_name
        self.id = menu.menu_id
        self.path = menu.menu_url
        self.icon = menu.menu_icon
        self.p_menu_id = menu.p_menu_id
        self.children = []


def get_menus(request):
    logger.info('获取菜单信息')
    start_time = time.time()
    try:
        menus = Menu.objects.all().order_by('menu_level', 'menu_order')
        ms = []
        for m in menus:
            menu_vo = MenuVO(m)
            ms.append(menu_vo)
        m_m = handler_menus(ms)
        json_str = json.dumps(m_m, default=lambda o: o.__dict__, sort_keys=True, ensure_ascii=False)
        # print(type(json_str))
        print(json_str)
        aaa = json.dumps({'code': 200, 'data': json.loads(json_str)})
        end_time = time.time()
        print(end_time - start_time)
        return HttpResponse(aaa, content_type='application/json')
        data = serializers.serialize('json', menus, ensure_ascii=False)
        # res = {'code': 200, 'message': data}
        return HttpResponse(data, content_type='application/json')
    except Menu.DoesNotExist:
        res = {'code': 100, 'message': '查询不到菜单信息'}
        return HttpResponse(json.dumps(res), content_type='application/json')


def handler_menus(menus):
    menu_son = []
    menu_father = []
    if len(menus) > 0:
        for menu in menus:
            if menu.path:
                menu_son.append(menu)
            else:
                menu_father.append(menu)
        for m1 in menu_son:
            for m2 in menu_father:
                if m1.p_menu_id == m2.id:
                    m2.children.append(m1)
        return menu_father
