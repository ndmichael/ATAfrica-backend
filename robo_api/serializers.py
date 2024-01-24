from rest_framework import serializers
from robo.models import RiskAssessment

class RoboSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskAssessment
        fields = (
            'risk_score', 'nigeria_stocks', 'foreign_stocks', 
            'teck_stocks', 'emerging_stocks', 'nigeria_bonds',
            'foreign_bonds', 'commodities', 'real_estate'  
        )