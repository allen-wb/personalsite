from django.db import models


# Create your models here.
class Menu(models.Model):
    menu_id = models.CharField(max_length=32, primary_key=True)
    menu_name = models.CharField(max_length=20)
    menu_level = models.IntegerField()
    menu_order = models.IntegerField()
    p_menu_id = models.CharField(max_length=32)
    menu_icon = models.CharField(max_length=50)
    menu_url = models.CharField(max_length=50)
    is_delete = models.IntegerField()
    remark = models.CharField(max_length=100)

    # @staticmethod
    # def __dict__(self):
    #     return {'menu_id': self.menu_id, 'menu_name': self.menu_name, 'p_menu_id': self.p_menu_id,
    #             'menu_icon': self.menu_icon, 'menu_url': self.menu_url, }
