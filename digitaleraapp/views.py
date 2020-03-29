from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .services import WebsiteAnalyzerService

from .serializers import BusinessInfoSerializer
from .models import BusinessInfo

class BusinessInfoViewSet(viewsets.ModelViewSet):
    queryset = BusinessInfo.objects.all()
    serializer_class = BusinessInfoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return BusinessInfo.objects.filter(owner=user)


@api_view(['POST'])
def analyzeUrlView(request):
    print('request', request.data['url'])
    phoneNumbers, emails, audits = WebsiteAnalyzerService.analyzeUrl(request.data['url'])
    return Response({'data':{
        'audits': audits,
        'phoneNumbers': phoneNumbers,
        'emails': emails
    }})