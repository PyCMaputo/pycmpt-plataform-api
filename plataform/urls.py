from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('member-api', views.MemberView)

urlpatterns = [
    path('api/', include(router.urls), name='url_api'),
]
