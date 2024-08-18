from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.View_Home, name='home'),
    path('Inventories/', views.List_Inventory, name='inventory-list'),
    path('Inventories/new/', views.Create_Inventory, name='inventory-create'),
    path('<int:pk>/', views.Detail_Inventory, name='inventory-detail'),
    path('<int:pk>/update/', views.Update_Inventory, name='inventory-update'),
    path('<int:pk>/delete/', views.Delete_Inventory, name='inventory-delete'),
    path('<int:pk>/new/', views.Create_RollerSkate, name='rollerskate-create'),
    path('<int:inventory_pk>/<int:pk>/detail/', views.Detail_RollerSkate, name='rollerskate-detail'),
    path('<int:inventory_pk>/<int:pk>/update/', views.Update_RollerSkate, name='rollerskate-update'),
    path('<int:inventory_pk>/<int:pk>/delete/', views.Delete_RollerSkate, name='rollerskate-delete'),
]

