__author__ = "Yuvi"

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopName"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="Contact"),
    path('tracker/', views.tracker, name="TrackingSetting"),
    path('search/', views.search, name="Search"),
    path('productview/', views.productview, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
    # path('/', views.index, name="ShopName"),
    # path('/', views.index, name="ShopName"),
]
