from django.conf.urls import patterns, include, url
from users.views import LoginView
from users.views import LoginProcessView

urlpatterns = patterns('',
                       url(r'^$', LoginView.as_view(), name="login"),
                       url(r'^login_process/$', LoginProcessView.as_view(), name="login_process"),
                    )
