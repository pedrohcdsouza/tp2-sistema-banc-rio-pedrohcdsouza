from django.db import models

class TipoTransferencia(models.IntegerChoices):
    TED = 1, 'TED'
    DOC = 2, 'DOC'
    PIX = 3, 'PIX'
    INTERNA = 4, 'Transferencia Interna'
    
class StatusOperacao(models.IntegerChoices):
    PROCESSANDO = 1, 'Processando'
    CONCLUIDA = 2, 'Concluída'
    FALHOU = 3, 'Falhou'

class TipoConta(models.IntegerChoices):
    CORRENTE = 1, 'Corrente'
    POUPANCA = 2, 'Poupança'
    SALARIO = 3, 'Salário'

class TipoDeposito(models.IntegerChoices):
    DINHEIRO = 1, 'Dinheiro'
    CHEQUE = 2, 'Cheque'
    TRANSFERENCIA = 3, 'Transferência'
    PIX = 4, 'PIX'

class LocalSaque(models.IntegerChoices):
    CAIXA = 1, 'Caixa'
    CAIXA_ELETRONICO = 2, 'Caixa Eletrônico'

class StatusOperacao(models.IntegerChoices):
    APROVADO = 1, 'Aprovado'
    NEGADO = 2, 'Negado'