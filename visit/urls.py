from django.urls import path

from .views import visit_create_view, visit_list_view

app_name = 'visit'

urlpatterns = [
    path('list/', visit_list_view, name='list'),
    path('create/', visit_create_view, name='create'),
]