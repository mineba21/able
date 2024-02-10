from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_eqplist/', views.get_eqplist, name='get_eqplist'),
    path('get_ppid/', views.get_ppid, name='get_ppid'),
    path('process_data/', views.process_data, name='process_data'),

]
