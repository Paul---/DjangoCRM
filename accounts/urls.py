from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage),
    path('products/', views.ProductsPage),
    path('customer/', views.CustomerPage),

]