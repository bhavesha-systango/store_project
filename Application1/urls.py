from django.contrib import admin
from django.urls import path
  
# importing views from views..py
from . import views
  
urlpatterns = [
    path('partner/', views.partner, name="partner"),
    path('addProduct/', views.addProduct, name = "addProduct"),
    path('updateProduct/<int:pk>', views.updateProduct, name = "updateProduct"),
    path('deleteProduct/<int:pk>', views.deleteProduct, name = "deleteProduct"),
    path('product/<int:pk>/', views.productDetail, name='productDetail'),
]

