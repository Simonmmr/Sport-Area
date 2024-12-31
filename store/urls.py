from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('login/', views.login_user, name="login"),
    path('search/', views.search, name="search"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('update_user/', views.update_user, name="update_user"),
    path('update_info/', views.update_info, name="update_info"),
    path('update_password/', views.update_password, name="update_password"),
    path('product/<int:pk>', views.product, name="product"),
    path('download/<int:pdf_id>/', views.download_pdf, name='download_pdf'),
    path('category/<str:space>', views.category, name="category"),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('contact/', views.contact_view, name='contact'),
]
