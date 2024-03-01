from .models import Execution
import requests as request

def scraping_PNCP():
    data = []
    response = request.get('https://pncp.gov.br/api/search/?tipos_documento=edital&ordenacao=-data&pagina=1&tam_pagina=10&status=recebendo_proposta')

    for contrato in response.json()['items']:
        
        list_itens = []
        itens = request.get(f"https://pncp.gov.br/api/pncp/v1/orgaos/{contrato['orgao_cnpj']}/compras/{contrato['ano']}/{contrato['numero_sequencial']}/itens?pagina=1&tamanhoPagina=5")
        for item in itens.json():
            
            obj = {
               'descricao': item['descricao'],
                'unidade': item['unidadeMedida'],
                'quantidade': item['quantidade'],
                'valor': item['valorUnitarioEstimado'],
                'valor_total': item['valorTotal'],
            }
            list_itens.append(obj)
        
        data.append({
            "descricao": contrato['description'],
            "comprador": contrato['orgao_nome'],
            "modalidade": contrato['modalidade_licitacao_nome'],
            "itens": list_itens
        })
        
    return data