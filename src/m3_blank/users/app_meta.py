#coding:utf-8
from django.conf import urls

from m3_ext.ui.app_ui import DesktopLoader, DesktopShortcut

from actions import UsersPack

from m3_ext.ui import app_ui
from m3.actions import ControllerCache
import controller

def register_actions():
    """
    Метод регистрации Action'ов для приложения в котором описан
    """
    controller.auth_controller.packs.append(
        UsersPack(),
    )



def register_desktop_menu():
    metarole = app_ui.GENERIC_USER

    users_pack = ControllerCache.find_pack(UsersPack)

    DesktopLoader.add(
        metarole,
        DesktopLoader.TOOLBOX,
        DesktopShortcut(
            pack=users_pack.logout_action,
            name=u'Выход',
            index=256
        )
    )


def register_urlpatterns():
    """
    Регистрация конфигурации урлов для приложения
    """
    return urls.defaults.patterns('',
        (r'^auth/', controller.auth_controller.process_request),
    )


# def register_metaroles(manager):
#     """
#     Функция возвращает список метаролей, которые регистрируются
#     по умолчанию на уровне Платформы М3.
#
#     @param manager: объект, отвечающий за управление метаролями.
#     """
#
#     # метароль Сотрудник
#     manager.TEACHER_METAROLE = UserMetarole(UserProfile.TEACHER, u'Сотрудник')
#     # метароль Родитель
#     manager.PARENT_METAROLE = UserMetarole(UserProfile.PARENT, u'Родитель')
#     # метароль обычного пользователя системы
#     manager.PUPIL_METAROLE = UserMetarole(UserProfile.PUPIL, u'Ученик')
#
#     return [
#         manager.TEACHER_METAROLE,
#         manager.PARENT_METAROLE,
#         manager.PUPIL_METAROLE
#     ]


