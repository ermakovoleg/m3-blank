# coding:utf-8
from objectpack import ObjectPack
from objectpack.tree_object_pack import TreeObjectPack
from objectpack import ui as api_ui

from models import Person, Institution
from controller import obs


class InstitutionTreeObjectPack(TreeObjectPack):
    """
    TreeObjectPack для модели Institution
    """

    model = Institution
    add_to_desktop = True
    short_name = 'institution'

    need_check_permission = True
    sub_permissions = {}
    sub_permissions['view'] = u'Просмотр'
    sub_permissions['add'] = u'Добавить'
    sub_permissions['edit'] = u'Изменить'
    sub_permissions['delete'] = u'Удалить'

    edit_window = add_window = api_ui.ModelEditWindow.fabricate(
        model=model,
        model_register=obs,
        field_list=[
            'name', 'parent', 'inn', 'kpp'
        ])

    def extend_menu(self, menu):
        return menu.SubMenu(
            u'Справочники',
            menu.Item(self.title, self.list_window_action),
        )


class PersonObjectPack(ObjectPack):
    """
    ObjectPack для модели Person
    """

    model = Person
    add_to_desktop = True
    short_name = 'person'

    edit_window = add_window = api_ui.ModelEditWindow.fabricate(
        model=model,
        model_register=obs
    )

    columns = [
        {
            'header': u'Фамилия',
            'data_index': 'surname',
        },
        {
            'header': u'Имя',
            'data_index': 'name',
        },
        {
            'header': u'Отчество',
            'data_index': 'patronymic',
        },
        {
            'header': u'Дата рождения',
            'data_index': 'date_of_birth',
        },
    ]

    need_check_permission = True

    sub_permissions = {}
    sub_permissions['view'] = u'Просмотр'
    sub_permissions['add'] = u'Добавить'
    sub_permissions['edit'] = u'Изменить'
    sub_permissions['delete'] = u'Удалить'

    def extend_menu(self, menu):
        return menu.SubMenu(
            u'Реестры',
            menu.Item(self.title, self.list_window_action),
        )




