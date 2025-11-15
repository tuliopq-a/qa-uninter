# 🔐 Auth Service – SGHSS

Serviço responsável por autenticação de usuários (pacientes, médicos, administradores).

---

## 📌 **Endpoints**

---

### **1. Health Check**

**GET** `/health`

Verifica se o serviço está funcionando.

#### ✔ Exemplo:

```bash
curl http://localhost:8001/health
```

---

### **2. Login**

**POST** `/login`

Realiza autenticação por CPF e senha.

#### 📥 **Parâmetros (query ou body)**

| Nome     | Tipo   | Obrigatório | Descrição                        |
| -------- | ------ | ----------- | -------------------------------- |
| cpf      | string | ✔           | CPF do usuário (somente números) |
| password | string | ✔           | Senha cadastrada                 |

#### ✔ Exemplo válido:

```bash
curl -X POST "http://localhost:8001/login?cpf=12345678901&password=senha123"
```

#### ✔ Resposta esperada:

```json
{
  "message": "Login realizado",
  "user": {
    "cpf": "12345678901",
    "role": "patient"
  }
}
```

---

## ⚠ Endpoint vulnerável (se habilitado)

Apenas se `VULNERABLE_MODE=True` no código.

```bash
curl -X POST "http://localhost:8001/login?cpf=12345678901&password=123' OR '1'='1"
```

---
