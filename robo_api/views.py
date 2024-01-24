from rest_framework import generics
from robo.models import RiskAssessment
from .serializers import RoboSerializer


class RoboList(generics.ListCreateAPIView):
    queryset = RiskAssessment.objects.all().order_by('-risk_score')
    serializer_class = RoboSerializer

class RoboDetails(generics.RetrieveAPIView):
    queryset = RiskAssessment.objects.all()
    serializer_class = RoboSerializer


