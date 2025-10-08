from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from banco.models import *
from banco.serializers import *

class AgenciaView(APIView):
    def get(self, request):
        agencias = Agencia.objects.all()
        serializer = AgenciaSerializer(agencias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AgenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class AgenciaDetailView(APIView):
    def get_object(self, pk):
        try:
            return Agencia.objects.get(pk=pk)
        except Agencia.DoesNotExist:
            return None

    def get(self, request, pk):
        agencia = self.get_object(pk)
        if agencia is None:
            return Response(status=404)
        serializer = AgenciaSerializer(agencia)
        return Response(serializer.data)

    def put(self, request, pk):
        agencia = self.get_object(pk)
        if agencia is None:
            return Response(status=404)
        serializer = AgenciaSerializer(agencia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        agencia = self.get_object(pk)
        if agencia is None:
            return Response(status=404)
        agencia.delete()
        return Response(status=204)

class ClienteView(APIView):
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ClienteDetailView(APIView):
    
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return None

    def get(self, request, pk):
        cliente = self.get_object(pk)
        if cliente is None:
            return Response(status=404)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    def put(self, request, pk):
        cliente = self.get_object(pk)
        if cliente is None:
            return Response(status=404)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        cliente = self.get_object(pk)
        if cliente is None:
            return Response(status=404)
        cliente.delete()
        return Response(status=204)

class ContaView(APIView):
    def get(self, request):
        contas = Conta.objects.all()
        serializer = ContaSerializer(contas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ContaDetailView(APIView):
    def get_object(self, pk):
        try:
            return Conta.objects.get(pk=pk)
        except Conta.DoesNotExist:
            return None

    def get(self, request, pk):
        conta = self.get_object(pk)
        if conta is None:
            return Response(status=404)
        serializer = ContaSerializer(conta)
        return Response(serializer.data)

    def put(self, request, pk):
        conta = self.get_object(pk)
        if conta is None:
            return Response(status=404)
        serializer = ContaSerializer(conta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        conta = self.get_object(pk)
        if conta is None:
            return Response(status=404)
        conta.delete()
        return Response(status=204)
    
class DepositoView(APIView):
    def get(self, request):
        depositos = Deposito.objects.all()
        serializer = DepositoSerializer(depositos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepositoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DepositoDetailView(APIView):
    def get_object(self, pk):
        try:
            return Deposito.objects.get(pk=pk)
        except Deposito.DoesNotExist:
            return None

    def get(self, request, pk):
        deposito = self.get_object(pk)
        if deposito is None:
            return Response(status=404)
        serializer = DepositoSerializer(deposito)
        return Response(serializer.data)

    def put(self, request, pk):
        deposito = self.get_object(pk)
        if deposito is None:
            return Response(status=404)
        serializer = DepositoSerializer(deposito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        deposito = self.get_object(pk)
        if deposito is None:
            return Response(status=404)
        deposito.delete()
        return Response(status=204)

class SaqueView(APIView):
    def get(self, request):
        saques = Saque.objects.all()
        serializer = SaqueSerializer(saques, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SaqueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class SaqueDetailView(APIView):
    def get_object(self, pk):
        try:
            return Saque.objects.get(pk=pk)
        except Saque.DoesNotExist:
            return None

    def get(self, request, pk):
        saque = self.get_object(pk)
        if saque is None:
            return Response(status=404)
        serializer = SaqueSerializer(saque)
        return Response(serializer.data)

    def put(self, request, pk):
        saque = self.get_object(pk)
        if saque is None:
            return Response(status=404)
        serializer = SaqueSerializer(saque, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        saque = self.get_object(pk)
        if saque is None:
            return Response(status=404)
        saque.delete()
        return Response(status=204)

class TransferenciaView(APIView):
    def get(self, request):
        transferencias = Transferencia.objects.all()
        serializer = TransferenciaSerializer(transferencias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransferenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class TransferenciaDetailView(APIView):
    def get_object(self, pk):
        try:
            return Transferencia.objects.get(pk=pk)
        except Transferencia.DoesNotExist:
            return None

    def get(self, request, pk):
        transferencia = self.get_object(pk)
        if transferencia is None:
            return Response(status=404)
        serializer = TransferenciaSerializer(transferencia)
        return Response(serializer.data)

    def put(self, request, pk):
        transferencia = self.get_object(pk)
        if transferencia is None:
            return Response(status=404)
        serializer = TransferenciaSerializer(transferencia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        transferencia = self.get_object(pk)
        if transferencia is None:
            return Response(status=404)
        transferencia.delete()
        return Response(status=204)