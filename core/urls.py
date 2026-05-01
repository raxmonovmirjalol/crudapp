from django.urls import path
from . import views

urlpatterns = [
    path('', views.ActionListView.as_view(), name='action-list'),
    path('actions/new/', views.ActionCreateView.as_view(), name='action-create'),
    path('actions/<int:pk>/edit/', views.ActionUpdateView.as_view(), name='action-update'),
    path('actions/<int:pk>/delete/', views.ActionDeleteView.as_view(), name='action-delete'),

    path('agendas/', views.AgendaListView.as_view(), name='agenda-list'),
    path('agendas/new/', views.AgendaCreateView.as_view(), name='agenda-create'),
    path('agendas/<int:pk>/edit/', views.AgendaUpdateView.as_view(), name='agenda-update'),
    path('agendas/<int:pk>/delete/', views.AgendaDeleteView.as_view(), name='agenda-delete'),
]
