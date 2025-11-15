# 🩺 Patient Service – SGHSS

Serviço responsável por cadastro e consulta de pacientes.

---

## 📌 **Endpoints**

---

### **1. Health Check**

**GET** `/health`

Verifica se o microserviço está rodando.

#### ✔ Exemplo:

```bash
curl http://localhost:8002/health
```

---

### **2. Listar Pacientes**

**GET** `/patients`

Retorna todos os pacientes cadastrados.

#### ✔ Exemplo:

```bash
curl http://localhost:8002/patients
```

#### ✔ Resposta esperada:

```json
[
  {
    "id": 1,
    "name": "João Silva",
    "cpf": "12345678901",
    "birth_date": "1990-04-12"
  },
  {
    "id": 2,
    "name": "Maria Oliveira",
    "cpf": "55566677788",
    "birth_date": "1985-10-20"
  }
]
```

---

### **3. Criar Paciente**

**POST** `/patients`

Cria um novo paciente.

#### 📥 **Parâmetros**

| Nome       | Tipo                | Obrigatório | Descrição                 |
| ---------- | ------------------- | ----------- | ------------------------- |
| name       | string              | ✔           | Nome completo do paciente |
| cpf        | string              | ✔           | CPF sem formatação        |
| birth_date | string (YYYY-MM-DD) | ✔           | Data de nascimento        |

#### ✔ Exemplo válido:

```bash
curl -X POST "http://localhost:8002/patients?name=Lucas%20Santos&cpf=44455566677&birth_date=1992-05-15"
```

#### ✔ Resposta esperada:

```json
{
  "message": "Paciente criado com sucesso",
  "cpf": "44455566677"
}
```

---
