from django.conf.urls import url

from django.contrib.auth.views import LoginView

from menus.views import (
        ItemCreateView,
        ItemDetailView,
        ItemListView,
        ItemUpdateView,
    )

urlpatterns = [
    #url(r'^(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='detail'),
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
    url(r'^$', ItemListView.as_view(), name='list'),
]
