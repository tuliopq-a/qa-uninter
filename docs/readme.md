## 📌 SGHSS-QA – Estrutura Inicial do Projeto

Este repositório contém a base do projeto **SGHSS (Sistema de Gestão Hospitalar e Serviços de Saúde)** para fins de testes e qualidade de software.
O foco é permitir testes funcionais, de desempenho e de segurança, conforme as diretrizes da disciplina.

---

# 🏗 Arquitetura Atual

A arquitetura utiliza **microserviços simulados (mock)** com **FastAPI**, todos rodando via **Docker**, mais um banco **MySQL** pré-populado.

```
/sghss-qa
 ├── docker-compose.yml
 ├── microservices/
 │    ├── auth-service/
 │    │    ├── main.py
 │    │    ├── Dockerfile
 │    │    ├── requirements.txt
 │    ├── patient-service/
 │    │    ├── main.py
 │    │    ├── Dockerfile
 │    │    ├── requirements.txt
 │    ├── appointment-service/
 │         ├── main.py
 │         ├── Dockerfile
 │         ├── requirements.txt
 ├── utils/
 │    └── generate_mock_data/
 │         └── init.sql
 └── docs/
      └── readme.md (este arquivo)
```

---

# 🗄 Banco de Dados

O MySQL é inicializado automaticamente e popula:

* Usuários (admin, doutor, paciente)
* Pacientes
* Agendamentos

Arquivo responsável:
`utils/generate_mock_data/init.sql`

---

# ▶ Como iniciar tudo

Pré-requisitos:

* Docker
* Docker Compose

Rodando:

```bash
docker-compose up --build
```

Serviços:

| Serviço             | Porta | Descrição                        |
| ------------------- | ----- | -------------------------------- |
| auth-service        | 8001  | Login e autenticação             |
| patient-service     | 8002  | Cadastro e listagem de pacientes |
| appointment-service | 8003  | Agendamentos                     |
| MySQL               | 3306  | Banco de dados                   |
