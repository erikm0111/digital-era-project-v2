from rest_framework import viewsets

from .serializers import BusinessInfoSerializer
from .models import BusinessInfo

class BusinessInfoViewSet(viewsets.ModelViewSet):
    queryset = BusinessInfo.objects.all().order_by('name')
    serializer_class = BusinessInfoSerializer