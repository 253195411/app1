from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view,name = 'login'),
    path('index', views.index,name = 'index'),
    path('logout', views.logout_view,name = 'login'),
    path('register',views.register,name = 'register'),
    path('customeradd', views.cust_add,name = 'customeradd'),
]