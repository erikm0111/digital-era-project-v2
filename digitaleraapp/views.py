from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .services import WebsiteAnalyzerService

from .serializers import BusinessInfoSerializer
from .models import BusinessInfo

class BusinessInfoViewSet(viewsets.ModelViewSet):
    queryset = BusinessInfo.objects.all().order_by('id')
    serializer_class = BusinessInfoSerializer

@api_view(['POST'])
def analyzeUrlView(request):
    print('request', request.data['url'])
    phoneNumbers, emails = WebsiteAnalyzerService.analyzeUrl(request.data['url'])
    return Response({'data':{
        'phoneNumbers': phoneNumbers,
        'emails': emails
    }})