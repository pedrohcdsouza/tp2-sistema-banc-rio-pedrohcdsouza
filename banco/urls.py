from banco.views import *
from django.urls import path

urlpatterns = [
    path('agencias/', AgenciaView.as_view(), name='agencia-list'),
    path('agencias/<int:pk>/', AgenciaDetailView.as_view(), name='agencia-detail'),
    path('clientes/', ClienteView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('contas/', ContaView.as_view(), name='conta-list'),
    path('contas/<int:pk>/', ContaDetailView.as_view(), name='conta-detail'),
    path('depositos/', DepositoView.as_view(), name='deposito-list'),
    path('depositos/<int:pk>/', DepositoDetailView.as_view(), name='deposito-detail'),
    path('saques/', SaqueView.as_view(), name='saque-list'),
    path('saques/<int:pk>/', SaqueDetailView.as_view(), name='saque-detail'),
    path('transferencias/', TransferenciaView.as_view(), name='transferencia-list'),
    path('transferencias/<int:pk>/', TransferenciaDetailView.as_view(), name='transferencia-detail'),
]