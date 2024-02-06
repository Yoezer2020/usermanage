from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('login')), name='index'),
    path('accounts/profile/', views.item_list, name='item_list'),
    path('item_list/', views.item_list, name='item_list'),
    path('add/', views.add_item, name='add_item'),
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit/<int:pk>/', views.edit_item, name='edit_item'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
