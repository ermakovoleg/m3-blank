# coding: utf-8

from django.contrib.auth import logout
from django.http import HttpResponse

from m3.actions import Action, ActionPack, PreJsonResult
from m3_ext.ui.shortcuts import MessageBox





class LogoutAction(Action):

    url = '/logout$'

    def run(self, request, context):
        confirm = request.REQUEST.get(u'confirm')

        # Подтверждение выхода
        if confirm == u'true':
            logout(request)
            return PreJsonResult({})
        # Возвращаем форму
        msg_box = MessageBox(u'', u'Вы действительно хотите выйти из системы?',
                             MessageBox.ICON_QUESTION, MessageBox.BTN_YESNO)
        msg_box.handler_yes = u'''
        Ext.Ajax.request({
            url: '%(url)s',
            params: {'confirm': true},
            success: function(response){
                var json = Ext.util.JSON.decode(response.responseText);
                window.location = json.redirect ? json.redirect : '/';
            }
        });
        ''' % {'url': self.get_absolute_url()}
        return HttpResponse(msg_box.get_script())




class UsersPack(ActionPack):
    url = '/auth'

    def __init__(self):
        super(UsersPack, self).__init__()
        self.logout_action = LogoutAction()

        self.actions.extend([
            self.logout_action,
        ])

    def get_logout_url(self):
        return self.logout_action.get_absolute_url()
