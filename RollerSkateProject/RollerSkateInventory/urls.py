from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('Inventories/', views.InventoryListView.as_view(), name='inventory-list'),
    path('Inventories/new/', views.InventoryCreateView.as_view(), name='inventory-create'),
    path('<int:pk>/', views.InventoryDetailView.as_view(), name='inventory-detail'),
    path('<int:pk>/update/', views.InventoryUpdateView.as_view(), name='inventory-update'),
    path('<int:pk>/delete/', views.InventoryDeleteView.as_view(), name='inventory-delete'),
    path('<int:pk>/new/', views.RollerSkateCreateView.as_view(), name='rollerskate-create'),
    path('<int:inventory_pk>/<int:pk>/detail/', views.RollerSkateDetailView.as_view(), name='rollerskate-detail'),
    path('<int:inventory_pk>/<int:pk>/update/', views.RollerSkateUpdateView.as_view(), name='rollerskate-update'),
    path('<int:inventory_pk>/<int:pk>/delete/', views.RollerSkateDeleteView.as_view(), name='rollerskate-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
