from django.conf.urls import url
from . import views
from app.views import delete_account

urlpatterns = [
    url('', views.index, name='per_user'),
    url('products', views.products, name='per_user-products'),
    url('profile', views.profile, name='per_user-profile'),
    url('edit-profile', views.edit_profile, name='per_useredit-profile'),
    url('delete-account', delete_account),
]