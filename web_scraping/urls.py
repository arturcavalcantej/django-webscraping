from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExecutionViewSet

router = DefaultRouter()
router.register(r'executions', ExecutionViewSet, basename='executions')  

urlpatterns = [
    path('', include(router.urls)),
]
