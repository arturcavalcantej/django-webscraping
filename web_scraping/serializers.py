from rest_framework import serializers
from .models import Execution

class ExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Execution
        fields = ['id', 'execution_date', 'execution_data', 'url_scraping', 'request_data', 'created', 'updated']
