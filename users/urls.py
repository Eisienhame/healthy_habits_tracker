from django.urls import path
from users.apps import UsersConfig

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

# urlpatterns = [
#
#     path('', LoginView.as_view(template_name='users/login.html'), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('profile/', ProfileUpdateView.as_view(), name='profile'),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('activate/<email>/', activate_user, name='activate'),
#     path('backup_pass', generate_pass, name='generate_password'),
#
# ]
