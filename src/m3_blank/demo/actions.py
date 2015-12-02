# coding:utf-8
from functools import partial

from m3 import actions as m3_actions

import objectpack
from objectpack import tree_object_pack
from objectpack.filters import FilterByField, ColumnFilterEngine

import models
import ui

class PersonObjectPack(objectpack.ObjectPack):
    """
    ObjectPack для модели Person
    """

    model = models.Person
    title = u'Физические лица'
    title_plural = u'Физические лица'
    add_to_desktop = True
    short_name = 'person'

    edit_window = add_window = objectpack.ui.ModelEditWindow.fabricate(model)

    def extend_menu(self, menu):
        return menu.SubMenu(
            u'Реестры',
            menu.Item(self.title, self.list_window_action),
        )


