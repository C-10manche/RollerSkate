from django.urls import path
from . import views

urlpatterns = [
    path('Events/', views.List_Event, name='event-list'),
    path('Events/new', views.Create_Event, name='event-create'),
    path('Events/<int:pk>/detail', views.Detail_Event, name='event-detail'),
    path('Events/<int:pk>/update', views.Update_Event, name='event-update'),
    path('Events/<int:pk>/delete', views.Delete_Event, name='event-delete'),
]

