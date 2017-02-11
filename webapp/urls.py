from django.conf.urls import url
from . import views
from . import mood_to_color

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^color$', views.color, name='color')
    ]
