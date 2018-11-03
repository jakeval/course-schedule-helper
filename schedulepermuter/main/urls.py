from django.urls import path, re_path, include

from . import views

urlpatterns = [
		path('', views.index, name='index'),
		path('ajax/add_slot', views.add_slot, name='add_slot'),
		path('ajax/render_slot_form', views.render_slot_form, name='render_slot_form'),
		re_path(r'^select2/', include('django_select2.urls')),
	]