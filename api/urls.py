from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Todoviewsets, UserViewSet

router = DefaultRouter()
router.register(r"todos", Todoviewsets, basename="todo")


router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("api/", include(router.urls)),
]
