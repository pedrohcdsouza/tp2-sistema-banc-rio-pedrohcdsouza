from django.db import models

from banco.types import LocalSaque, StatusOperacao, TipoConta, TipoDeposito, TipoTransferencia

class Agencia(models.Model):
    agencia_id = models.IntegerField(unique=True)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    gerente = models.CharField(max_length=255)
    status = models.BooleanField()

class Cliente(models.Model):
    cpf = models.IntegerField(unique=True)
    nome = models.CharField(max_length=255)
    dtanascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    dtacadastro = models.DateField()
    status = models.BooleanField()


class Conta(models.Model):
    nro = models.IntegerField(unique=True)
    agencia = models.IntegerField()
    cpf = models.IntegerField(unique=True)
    tipo = models.IntegerField(choices=TipoConta.choices)
    saldo = models.FloatField()
    dtaabertura = models.DateField()
    status = models.BooleanField()
    limite_diario = models.FloatField()


class Deposito(models.Model):
    
    nro_conta = models.IntegerField()
    valor = models.FloatField()
    data = models.DateTimeField()
    tipo = models.IntegerField(choices=TipoDeposito.choices)
    descricao = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)


class Saque(models.Model):
    
    nro_conta = models.IntegerField()
    valor = models.FloatField()
    data = models.DateTimeField()
    local = models.IntegerField(choices=LocalSaque.choices)
    descricao = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255, blank=True, null=True)
    status_operacao = models.IntegerField(choices=StatusOperacao.choices)


class Transferencia(models.Model):
    nro_origem = models.IntegerField()
    nro_destino = models.IntegerField()
    valor = models.FloatField()
    data = models.DateTimeField()
    tipo = models.IntegerField(choices=TipoTransferencia.choices)
    descricao = models.CharField(max_length=255)
    status_operacao = models.IntegerField(choices=StatusOperacao.choices)
