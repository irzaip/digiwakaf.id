from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.homePage, name="home"),
    path('asset/', views.assetPage, name='asset'),
    path('asset/<str:sid>/', views.lookupassetPage, name='lookupAsset'),
    path('customer/', views.customer, name='customer'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name="logout"),
]
