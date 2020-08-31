from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recipe_id>/', views.detail, name='detail'),
    path('new', views.new, name='new'),
    path('new_from_web', views.new_from_web, name='new-from-web'),
]
