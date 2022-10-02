from django.urls import include, path
from rest_framework import routers

from cotization_api.views import DollarViewSet

#from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'Dollar', DollarViewSet)

urlpatterns = [
   path('', include(router.urls)),
]