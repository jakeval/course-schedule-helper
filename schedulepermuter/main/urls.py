from django.urls import path, re_path, include

from . import views

urlpatterns = [
		path('', views.index, name='index'),
		re_path(r'^select2/', include('django_select2.urls')),
	]