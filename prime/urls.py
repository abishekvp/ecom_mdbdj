from django.conf.urls import url
from . import views
from app.views import delete_account

urlpatterns = [
    url('', views.index, name='prime'),
    url('profile', views.profile, name='prime-profile'),
    url('edit-profile', views.edit_profile, name='prime-edit-profile'),
    url('products', views.products, name='prime-products'),
    url('delete-account', delete_account, name='delete-account'),
]