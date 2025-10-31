from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_blog, name='create_blog'),
    path('update/<int:id>/', views.update_blog, name='create_blog'),
    path('delete/<int:id>/',views.delete_blog),
    path('about/',views.about_info_blog),
    path('area/',views.area_blog),
    path('area_create/', views.area_create_blog, name='area_blog'),
    path('area_update/<int:id>/', views.area_update_blog),
    path('area_delete/<int:id>/',views.area_delete_blog),
    path('city/',views.city_blog),
    path('city_create/', views.city_create_blog, name='city_blog'),
    path('city_update/<int:id>/', views.city_update_blog),
    path('city_delete/<int:id>/',views.city_delete_blog),

]


