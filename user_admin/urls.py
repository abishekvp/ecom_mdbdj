from django.conf.urls import url
from . import views
from app.views import delete_account

urlpatterns = [
    url('', views.index, name='user-admin'),
    url('create-product', views.create_product, name='create-product'),
    url('view-products', views.view_products, name='view-products'),
    url('edit-product/<str:pc>/', views.edit_product, name='edit-product'),
    url('delete-product/<str:pc>/', views.delete_product, name='delete-product'),
    
    url('clients', views.clients, name='clients'),
    url('approve-user/<str:email>/', views.approve_user, name='approve-user'),
    url('revoke-user/<str:email>/', views.revoke_user, name='revoke-user'),
    url('remove-user/<str:email>/', views.remove_user, name='remove-user'),
    
    url('profile', views.profile, name='user-admin-profile'),
    url('edit-profile', views.edit_profile, name='user-admin-edit-profile'),
    
    url('delete-account', delete_account, name='delete-account'),
]