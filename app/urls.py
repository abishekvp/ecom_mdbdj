from django.conf.urls import url
from . import views


urlpatterns = [
    url('',views.index,name="index"),
    url('signup',views.signup,name="signup"),
    url('signin',views.signin,name="signin"),
    url('signout',views.signout,name="signout"),
    url('authenticating-user',views.auth_user,name="auth_user"),
    url('error',views.error,name="error"),
    
    url('test',views.test,name="test"),
    
    url('delete-account',views.delete_account,name="delete-account"),   
]
