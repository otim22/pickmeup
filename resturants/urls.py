from django.conf.urls import url

from django.contrib.auth.views import LoginView

from resturants.views import (
        ResturantListView,
        ResturantDetailView,
        ResturantCreateView,
        ResturantUpdateView
    )

urlpatterns = [
    url(r'^create/$', ResturantCreateView.as_view(), name='create'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', ResturantDetailView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/$', ResturantUpdateView.as_view(), name='detail'),
    url(r'^$', ResturantListView.as_view(), name='list'),
]
