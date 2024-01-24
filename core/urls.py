
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('robo.urls', namespace='robo')),
    path('api/', include('robo_api.urls', namespace='robo_api'))

]
