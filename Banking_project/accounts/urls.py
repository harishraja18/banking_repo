from django.urls import path
from . import views as this_is_accounts

urlpatterns = [
    path('',this_is_accounts.login_page, name='login'),
    path('logout_page/',this_is_accounts.logout_page, name='logout'),
    path('register/',this_is_accounts.register, name='register'),
    path('profile/',this_is_accounts.profile, name='profile')
]