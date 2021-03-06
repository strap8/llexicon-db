from django.urls import path, include
from .views import UserView, SettingView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserView)
router.register('user/settings', SettingView)

urlpatterns = [
    path('', include(router.urls))
]
