from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import include, path

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("users", UserViewSet)

urls = [
    path("users/", include('lexbot.users.urls')),
]


app_name = "api"
urlpatterns = router.urls + urls
