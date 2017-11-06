from django.conf.urls import url

from . import views

# Once mapped assure that root URLconf points to polls.urls
urlpatterns = [
    url(r'^$', views.index, name='index'),
]