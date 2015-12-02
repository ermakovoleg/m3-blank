# coding:utf-8
from functools import partial

from m3 import actions as m3_actions

import objectpack
from objectpack import tree_object_pack
from objectpack.filters import FilterByField, ColumnFilterEngine

import models
import ui


# =============================================================================
# PersonObjectPack
# =============================================================================
class PersonObjectPack(objectpack.ObjectPack):
    """
    ObjectPack для модели Person
    """

    model = models.Person
    title = u'Дети в системе'
    width = 1200
    height = 700


    # add_to_desktop = True
    # add_to_menu = True
    #
    short_name = 'person'
    # url = '/person'
    # title = u'Физические лица'
    # title_plural = u'Физические лица'


    # edit_window = add_window = objectpack.ui.ModelEditWindow.fabricate(model)


