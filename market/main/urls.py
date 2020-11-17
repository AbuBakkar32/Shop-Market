from django.urls import path
from main import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('item/', views.itempage, name='item'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('register/', views.registerpage, name='register'),
    path('order/', views.order, name='order'),
    path('order_cancel/', views.orderCancel, name='orderCancel'),
]
