from django.shortcuts import render
import json
from rest_framework.response import Response


# Create your views here.
from rest_framework import viewsets
from .models import Execution
from .serializers import ExecutionSerializer
from .utils import *

class ExecutionViewSet(viewsets.ModelViewSet):
    queryset = Execution.objects.all()
    serializer_class = ExecutionSerializer

    def retrieve(self, request, pk=None):
        execution = Execution.objects.get(pk=pk)
        if execution.url_scraping == 'https://pncp.gov.br/app/editais?q=&&status=recebendo_proposta&pagina=1':
            execution.execution_data = json.dumps(scraping_PNCP())

        execution.save()
        return Response({'message': 'Leitura de dados executada com sucesso'})

