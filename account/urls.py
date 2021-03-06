from django.urls import path, include
from django.contrib.auth import views as auth_views
from account.views import (user_login, dashboard, register, edit, user_list, user_details,
                           user_follow)

# urlpatterns = [
#     path('', include('django.contrib.auth.urls'))
# ]

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('edit/', edit, name='edit'),
    path('register/', register, name='register'),
    path('custom_login/', user_login, name='custom_login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('users/', user_list, name='user_list'),
    path('users/follow/', user_follow, name='user_follow'),
    path('users/<str:username>/', user_details, name='user_details'),
]
