from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^category/(?P<cat_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^category/(?P<cat_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    )
