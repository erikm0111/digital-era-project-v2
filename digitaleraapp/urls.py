from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'businessInfos', views.BusinessInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^analyzeUrl/$', views.analyzeUrlView),
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

]