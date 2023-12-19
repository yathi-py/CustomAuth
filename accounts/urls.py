from django.urls import path
from accounts.views import SignupView, LoginView, logout_user

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', logout_user, name='logout'),
]

