from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^get_recommendation/$', views.get_recommendation, name='get_recommendation'),
        url(r'^display_meta/$', views.display_meta, name='display_meta'),
        # url(r'^(?P<search_word>.+)/$', views.results, name='results'),
        ]
