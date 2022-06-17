from django.urls import path
from django.urls import include, path
from lexbot.users.views import UserAuthView, UserInfoProfileView

app_name = "users"
url = [
    path('register/', UserAuthView.as_view(),name='register'),
    path('user-info/<int:pk>/', UserInfoProfileView.as_view(), name='user-info'),
]

urlpatterns = url
