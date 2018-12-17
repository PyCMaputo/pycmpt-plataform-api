from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('accounts-api', views.UserAPI)


urlpatterns = [
    path('', views.account, name='url_account'),
    path('create/', views.create_account, name='url_create_account'),
    path('login/', views.login_view, name='url_login'),
    path('logout/', views.logout_view, name='url_logout'),
    path('api/', include(router.urls), name='url_accounts_api'),
]
