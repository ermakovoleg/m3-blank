# coding: utf-8

from django.conf import urls
from m3_ext.ui import app_ui
from m3.actions import ControllerCache
from objectpack import desktop

from m3_ext.ui.app_ui import DesktopLoader, DesktopShortcut

from actions import PersonObjectPack
import controller



def register_urlpatterns():
    """
    Регистрация конфигурации урлов для приложения
    """
#     return urls.defaults.patterns(
#         "",
#
#         controller.action_controller._url_patterns
#     )

    return urls.defaults.patterns(
            '',
            ('^', controller.action_controller.process_request),
        )

def register_actions():
    """
    регистрация экшенов
    """
    controller.action_controller.packs.append(PersonObjectPack())


# def register_desktop_menu():
#     """
#     регистрация элеметов рабочего стола
#     """
#
#     # pack = ControllerCache.find_pack(actions.PersonObjectPack)
#     #
#     # metarole = app_ui.GENERIC_USER
#     #
#     #
#     #
#     # persons_shortcut = DesktopShortcut(
#     #     name=u'Физические лицаца',
#     #     pack=pack)
#     # DesktopLoader.add(
#     #     metarole, DesktopLoader.TOPTOOLBAR, persons_shortcut)
#     # DesktopLoader.add(
#     #     metarole, DesktopLoader.START_MENU, persons_shortcut)
#     #
#     # # menu_root.dicts()
#
#     desktop.uificate_the_controller(controller.action_controller)



