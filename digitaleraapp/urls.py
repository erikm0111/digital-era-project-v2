from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'businessInfos', views.BusinessInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('analyzeUrl/', views.analyzeUrlView),
    path('users/', include('users.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),

]