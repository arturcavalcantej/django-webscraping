from django.contrib import admin
from .models import Execution
from django.utils.html import format_html
from django.urls import path
from django.urls import reverse
from .utils import *
from django.shortcuts import redirect
import json

class ExecutionAdmin(admin.ModelAdmin):
    list_display = ('execution_date', 'url_scraping', 'created', 'updated', ) 
    search_fields = ('url_scraping',)
    readonly_fields = ('id', 'created', 'updated', 'execution_date')
    actions = ['custom_action']

    fieldsets = (
        (None, {
            'fields': ('url_scraping','execution_date' )
        }),
        ('Dados Avançados', {
            'classes': ('collapse',),
            'fields': ('execution_data', 'request_data'),
        }),
    )

    def custom_action(self, request, queryset):
        for obj in queryset:
            if obj.url_scraping == 'https://pncp.gov.br/app/editais?q=&&status=recebendo_proposta&pagina=1':
                obj.execution_data = json.dumps(scraping_PNCP())

            obj.save()
        self.message_user(request, "Os dados foram atualizados com sucesso para os objetos selecionados.")

    

   

admin.site.register(Execution, ExecutionAdmin)