# coding: utf-8

from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from m3.actions import Action, ActionPack, PreJsonResult
from m3_ext.ui.shortcuts import MessageBox


# from web_edu.views import get_background_url
# from web_edu.core.app_settings.helpers import get_inline_code
# from web_edu.core.users.models import UserProfile


# class LoginPageAction(Action):
#
#     u"""Отображение страницы входа в систему."""
#
#     url = '/login-page'
#     template_file_name = 'main.html'
#
#     def _get_template_context(self, request):
#         user = request.user
#         profile = None
#         if user.is_authenticated():
#             profile = user.get_profile()
#
#         return dict(
#             user=user,
#             profile=profile,
#             pupil_role=UserProfile.PUPIL,
#             login_url=self.parent.get_login_url(),
#             logout_url=self.parent.get_logout_url(),
#             sia_login_url=self.parent.get_sia_login_url(),
#             active_menu='diary',
#             is_demo_login=settings.WEB_EDU_DEMO_LOGIN,
#             demo_users=settings.WEB_EDU_DEMO_USERS,
#             message=request.GET.get('message'),
#             background_path=get_background_url(suffix='_login'),
#             inlines=get_inline_code(request),
#             USE_SIA=settings.USE_SIA,
#             SYSTEM_LOGO=settings.SYSTEM_LOGO,
#             FORGET_PASSWORD_ON=settings.FORGET_PASSWORD_ON,
#             page_title=settings.PAGE_TITLE,
#             description=settings.DESCRIPTION,
#             keywords=settings.KEYWORDS,
#         )
#
#     def run(self, request, context):
#         template_context = self._get_template_context(request)
#         return render_to_response(self.template_file_name, template_context)


# class LoginAction(Action):
#     url = '/login'
#
#     def context_declaration(self):
#         return [
#             ActionContextDeclaration(name='login_login', type=str, default='',
#                                      required=True),
#             ActionContextDeclaration(name='login_password', type=str, default='',
#                                      required=True)
#         ]
#
#     def run(self, request, context):
#         u"""
#             Выполнение авторизации
#         """
#
#
#         login = context.login_login
#         password = context.login_password
#
#
#         return None


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
        # self.login_page_action = LoginPageAction()
        # self.login_action = LoginAction()
        self.logout_action = LogoutAction()

        self.actions.extend([
            # self.login_page_action,
            # self.login_action,
            self.logout_action,
        ])

    # def get_login_url(self):
    #     return self.login_action.get_absolute_url()

    def get_logout_url(self):
        return self.logout_action.get_absolute_url()
