from django.db import models
from django.utils import timezone


class RiskAssessment(models.Model):
    risk_score= models.IntegerField(primary_key=True)
    nigeria_stocks= models.CharField(max_length=50)
    foreign_stocks= models.CharField(max_length=50)
    teck_stocks= models.CharField(max_length=50, default="0%")
    emerging_stocks= models.CharField(max_length=50)
    nigeria_bonds= models.CharField(max_length=50)
    foreign_bonds= models.CharField(max_length=50)
    commodities= models.CharField(max_length=50)
    real_estate= models.CharField(max_length=50)
    t_bills= models.CharField(max_length=50, default="0%")
    alternative= models.CharField(max_length=50, default="0%")

    def __str__(self):
        return f"{self.risk_score}"
