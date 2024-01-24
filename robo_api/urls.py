from django.urls import path, include
from .views import RoboDetails, RoboList


app_name = 'robo_api'

urlpatterns = [
    path('robo', RoboList.as_view(), name='robo_list'),
    path('robo/<int:pk>', RoboDetails.as_view(), name='robo_detail')
    
]