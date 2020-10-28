from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import BookViewSet, CopyViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('copies', CopyViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('',include(router.urls))
]