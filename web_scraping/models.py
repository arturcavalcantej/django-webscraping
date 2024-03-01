from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField('Data Criação', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Data Atualização', auto_now=True, auto_now_add=False)
    class Meta:
        abstract = True

choices_urls = [
    ('http://www.infraestrutura.mg.gov.br/ajuda/page/44-preco-setop', 'SETOP'),
    ('http://www.infraestrutura.mg.gov.br/component/gmg/page/102-c', 'INFRA MG'),
    ('https://pncp.gov.br/app/editais?q=&&status=recebendo_proposta&pagina=1', 'PNCP'),
    ('https://licitacoes.caixa.gov.br/', 'CAIXA'),
]

class Execution(BaseModel):
    execution_date = models.DateTimeField(null=True, blank=True)
    execution_data = models.TextField(null=True, blank=True)
    url_scraping = models.CharField(max_length=200, choices=choices_urls)  
    request_data = models.TextField(null=True, blank=True)



