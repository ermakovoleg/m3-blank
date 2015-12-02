# coding:utf-8
"""
Обсервер и контроллеры
"""

from objectpack import observer

obs = observer.Observer()

main_controller = observer.ObservableController(obs, "/controller")
