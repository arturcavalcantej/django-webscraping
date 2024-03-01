from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExecutionViewSet

# Altere sua configuração de URLs para incluir o nome da rota para a view ExecutionViewSet
router = DefaultRouter()
router.register(r'executions', ExecutionViewSet, basename='executions')  

urlpatterns = [
    path('', include(router.urls)),
    # Se houver outras URLs, inclua-as aqui
]