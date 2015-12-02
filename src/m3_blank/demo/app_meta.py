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

    return urls.defaults.patterns(
            '',
            ('^', controller.action_controller.process_request),
        )

def register_actions():
    """
    регистрация экшенов
    """
    controller.packs.append(PersonObjectPack())


def register_desktop_menu():
    """
    регистрация элеметов рабочего стола
    """

    desktop.uificate_the_controller(controller.action_controller)



