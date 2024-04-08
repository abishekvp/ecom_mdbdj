from django.conf.urls import url
from . import views
from app.views import delete_account

urlpatterns = [
    url('', views.index, name='plumber'),
    url('profile', views.profile, name='plumber-profile'),
    url('edit-profile', views.edit_profile, name='plumber-edit-profile'),
    url('products', views.products, name='plumber-products'),
    url('delete-account', delete_account, name='delete-account'),
]