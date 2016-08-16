from django.conf.urls import url

from . import views
from . import analysis

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^visits/', views.detail, name='visits'),
    #url(r'^visits/(?P<month>[A-Z][a-z]+)\.(?P<day>\d+)\,(?P<year>\d{4}\,d{1}\:\d{2})', views.detail, name='detail'),
    url(r'^analysis/$', analysis.chart_view, name='analysis'),
    url(r'^login/$', views.user_login, name='login'),
    ]

#(?P<month>[A-Z][a-z]+)\.(?P<day>\d+)\,(?P<year>\d{4}\,d{1}\:\d{2})+)