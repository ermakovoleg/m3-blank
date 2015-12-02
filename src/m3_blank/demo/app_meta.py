# coding: utf-8

from django.conf import urls
from objectpack import desktop

from actions import PersonObjectPack, InstitutionTreeObjectPack
import controller



def register_urlpatterns():
    """
    Регистрация конфигурации урлов для приложения
    """

    return urls.defaults.patterns(
            '',
            ('^', controller.main_controller.process_request),
        )

def register_actions():
    """
    регистрация экшенов
    """
    controller.main_controller.extend_packs(
        (
            PersonObjectPack(),
            InstitutionTreeObjectPack(),
        ))


def register_desktop_menu():
    """
    регистрация элеметов рабочего стола
    """

    desktop.uificate_the_controller(controller.main_controller)



