from django.conf.urls import url
from users.views import LoginView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
]