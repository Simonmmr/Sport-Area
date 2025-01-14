from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('category/<str:space>', views.category, name="category"),
    path('contact/', views.contact_view, name='contact'),
    path('post_form/', views.post_form, name='post_form'),
    path('view_detail/<int:pk>/', views.view_detail, name='view_detail'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
]