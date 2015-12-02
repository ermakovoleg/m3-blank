# coding:utf-8
"""
Обсервер и контроллеры
"""

from objectpack import observer



# Наблюдатель
obs = observer.Observer()

action_controller = observer.ObservableController(obs, "/controller")


# from m3.actions import ActionController

# action_controller = ActionController(url='/dicts', name=u'Справочники')

# from objectpack import observer
#
# main_controller = observer.ObservableController(core_observer, '/actions')