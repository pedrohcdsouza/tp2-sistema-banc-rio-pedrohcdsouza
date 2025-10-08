# Sistema Bancário - API REST

## Descrição do Projeto

Este projeto é uma API REST desenvolvida com Django e Django REST Framework para simular um sistema bancário completo. O sistema permite gerenciar agências, clientes, contas bancárias e operações financeiras como depósitos, saques e transferências.

### Funcionalidades Principais

- **Gestão de Agências**: Cadastro e gerenciamento de agências bancárias
- **Gestão de Clientes**: Cadastro e controle de clientes do banco
- **Gestão de Contas**: Criação e administração de contas bancárias (Corrente, Poupança, Salário)
- **Operações Financeiras**: 
  - Depósitos (Dinheiro, Cheque, Transferência, PIX)
  - Saques (Caixa, Caixa Eletrônico)
  - Transferências (TED, DOC, PIX, Transferência Interna)

### Tecnologias Utilizadas

- Python 3.x
- Django 5.2
- Django REST Framework
- PosgreSQL 17
- drf-yasg (documentação Swagger/OpenAPI)

## Descrição dos Modelos

### 1. Agencia
Representa uma agência bancária no sistema.

**Campos:**
- `agencia_id`: ID único da agência (IntegerField, unique=True)
- `nome`: Nome da agência (CharField, max_length=255)
- `endereco`: Endereço da agência (CharField, max_length=255)
- `telefone`: Telefone de contato (CharField, max_length=255)
- `gerente`: Nome do gerente responsável (CharField, max_length=255)
- `status`: Status ativo/inativo da agência (BooleanField)

### 2. Cliente
Representa um cliente do banco.

**Campos:**
- `cpf`: CPF do cliente (IntegerField, unique=True)
- `nome`: Nome completo do cliente (CharField, max_length=255)
- `dtanascimento`: Data de nascimento (DateField)
- `endereco`: Endereço residencial (CharField, max_length=255)
- `telefone`: Telefone de contato (CharField, max_length=255)
- `dtacadastro`: Data de cadastro no sistema (DateField)
- `status`: Status ativo/inativo do cliente (BooleanField)

### 3. Conta
Representa uma conta bancária.

**Campos:**
- `nro`: Número da conta (IntegerField, unique=True)
- `agencia`: ID da agência (IntegerField)
- `cpf`: CPF do titular (IntegerField, unique=True)
- `tipo`: Tipo da conta (IntegerField com choices)
  - 1: Corrente
  - 2: Poupança
  - 3: Salário
- `saldo`: Saldo atual da conta (FloatField)
- `dtaabertura`: Data de abertura da conta (DateField)
- `status`: Status ativo/inativo da conta (BooleanField)
- `limite_diario`: Limite diário para operações (FloatField)

### 4. Deposito
Representa uma operação de depósito.

**Campos:**
- `nro_conta`: Número da conta de destino (IntegerField)
- `valor`: Valor do depósito (FloatField)
- `data`: Data e hora da operação (DateTimeField)
- `tipo`: Tipo do depósito (IntegerField com choices)
  - 1: Dinheiro
  - 2: Cheque
  - 3: Transferência
  - 4: PIX
- `descricao`: Descrição da operação (CharField, max_length=255)
- `responsavel`: Responsável pela operação (CharField, max_length=255)

### 5. Saque
Representa uma operação de saque.

**Campos:**
- `nro_conta`: Número da conta de origem (IntegerField)
- `valor`: Valor do saque (FloatField)
- `data`: Data e hora da operação (DateTimeField)
- `local`: Local do saque (IntegerField com choices)
  - 1: Caixa
  - 2: Caixa Eletrônico
- `descricao`: Descrição da operação (CharField, max_length=255)
- `responsavel`: Responsável pela operação (CharField, max_length=255, opcional)
- `status_operacao`: Status da operação (IntegerField com choices)
  - 1: Aprovado
  - 2: Negado

### 6. Transferencia
Representa uma operação de transferência entre contas.

**Campos:**
- `nro_origem`: Número da conta de origem (IntegerField)
- `nro_destino`: Número da conta de destino (IntegerField)
- `valor`: Valor da transferência (FloatField)
- `data`: Data e hora da operação (DateTimeField)
- `tipo`: Tipo da transferência (IntegerField com choices)
  - 1: TED
  - 2: DOC
  - 3: PIX
  - 4: Transferência Interna
- `descricao`: Descrição da operação (CharField, max_length=255)
- `status_operacao`: Status da operação (IntegerField com choices)
  - 1: Processando
  - 2: Concluída
  - 3: Falhou

## Descrição dos Endpoints

A API segue o padrão RESTful e está disponível no prefixo `/api/`. Todos os endpoints suportam operações CRUD completas.

### Base URL
```
http://localhost:8000/api/
```

### 1. Agências

#### Listar todas as agências
- **GET** `/api/agencias/`
- **Resposta**: Lista de todas as agências cadastradas

#### Criar nova agência
- **POST** `/api/agencias/`
- **Body**: JSON com dados da agência
```json
{
    "agencia_id": 1001,
    "nome": "Agência Centro",
    "endereco": "Rua Principal, 123",
    "telefone": "(11) 1234-5678",
    "gerente": "João Silva",
    "status": true
}
```

#### Buscar agência específica
- **GET** `/api/agencias/{id}/`
- **Resposta**: Dados da agência especificada

#### Atualizar agência
- **PUT** `/api/agencias/{id}/`
- **Body**: JSON com dados atualizados da agência

#### Deletar agência
- **DELETE** `/api/agencias/{id}/`
- **Resposta**: 204 No Content

### 2. Clientes

#### Listar todos os clientes
- **GET** `/api/clientes/`

#### Criar novo cliente
- **POST** `/api/clientes/`
- **Body**: JSON com dados do cliente
```json
{
    "cpf": 12345678901,
    "nome": "Maria Santos",
    "dtanascimento": "1990-05-15",
    "endereco": "Rua das Flores, 456",
    "telefone": "(11) 9876-5432",
    "dtacadastro": "2024-01-15",
    "status": true
}
```

#### Buscar cliente específico
- **GET** `/api/clientes/{id}/`

#### Atualizar cliente
- **PUT** `/api/clientes/{id}/`

#### Deletar cliente
- **DELETE** `/api/clientes/{id}/`

### 3. Contas

#### Listar todas as contas
- **GET** `/api/contas/`

#### Criar nova conta
- **POST** `/api/contas/`
- **Body**: JSON com dados da conta
```json
{
    "nro": 123456,
    "agencia": 1001,
    "cpf": 12345678901,
    "tipo": 1,
    "saldo": 1000.00,
    "dtaabertura": "2024-01-15",
    "status": true,
    "limite_diario": 500.00
}
```

#### Buscar conta específica
- **GET** `/api/contas/{id}/`

#### Atualizar conta
- **PUT** `/api/contas/{id}/`

#### Deletar conta
- **DELETE** `/api/contas/{id}/`

### 4. Depósitos

#### Listar todos os depósitos
- **GET** `/api/depositos/`

#### Registrar novo depósito
- **POST** `/api/depositos/`
- **Body**: JSON com dados do depósito
```json
{
    "nro_conta": 123456,
    "valor": 200.00,
    "data": "2024-01-15T10:30:00Z",
    "tipo": 1,
    "descricao": "Depósito em dinheiro",
    "responsavel": "Caixa 01"
}
```

#### Buscar depósito específico
- **GET** `/api/depositos/{id}/`

#### Atualizar depósito
- **PUT** `/api/depositos/{id}/`

#### Deletar depósito
- **DELETE** `/api/depositos/{id}/`

### 5. Saques

#### Listar todos os saques
- **GET** `/api/saques/`

#### Registrar novo saque
- **POST** `/api/saques/`
- **Body**: JSON com dados do saque
```json
{
    "nro_conta": 123456,
    "valor": 150.00,
    "data": "2024-01-15T14:20:00Z",
    "local": 2,
    "descricao": "Saque no caixa eletrônico",
    "responsavel": null,
    "status_operacao": 1
}
```

#### Buscar saque específico
- **GET** `/api/saques/{id}/`

#### Atualizar saque
- **PUT** `/api/saques/{id}/`

#### Deletar saque
- **DELETE** `/api/saques/{id}/`

### 6. Transferências

#### Listar todas as transferências
- **GET** `/api/transferencias/`

#### Registrar nova transferência
- **POST** `/api/transferencias/`
- **Body**: JSON com dados da transferência
```json
{
    "nro_origem": 123456,
    "nro_destino": 654321,
    "valor": 300.00,
    "data": "2024-01-15T16:45:00Z",
    "tipo": 3,
    "descricao": "Transferência PIX",
    "status_operacao": 2
}
```

#### Buscar transferência específica
- **GET** `/api/transferencias/{id}/`

#### Atualizar transferência
- **PUT** `/api/transferencias/{id}/`

#### Deletar transferência
- **DELETE** `/api/transferencias/{id}/`

## Documentação da API

O projeto inclui documentação automática da API usando Swagger/OpenAPI:

- **Swagger UI**: `http://localhost:8000/swagger/`
- **ReDoc**: `http://localhost:8000/redoc/`

## Como Executar o Projeto

1. **Instalar dependências**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Executar migrações**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Criar superusuário** (opcional):
   ```bash
   python manage.py createsuperuser
   ```

4. **Executar servidor**:
   ```bash
   python manage.py runserver
   ```

5. **Acessar a API**:
   - API: `http://localhost:8000/api/`
   - Admin: `http://localhost:8000/admin/`
   - Swagger: `http://localhost:8000/swagger/`

## Estrutura do Projeto

```
tp2-sistema-banc-rio-pedrohcdsouza/
├── manage.py
├── requirements.txt
├── README.md
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── banco/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── serializers.py
    ├── urls.py
    ├── types.py
    ├── tests.py
    └── migrations/
```
