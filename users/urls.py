from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserAdminViewSet, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'gerente/users', UserAdminViewSet, basename='user-admin')

urlpatterns = [
    path('', include(router.urls)),
]
