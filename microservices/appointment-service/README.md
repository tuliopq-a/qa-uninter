# 📅 Appointment Service – SGHSS

Serviço responsável por agendamentos de consultas.

---

## 📌 **Endpoints**

---

### **1. Health Check**

**GET** `/health`

Verifica funcionamento do microserviço.

#### ✔ Exemplo:

```bash
curl http://localhost:8003/health
```

---

### **2. Listar Agendamentos**

**GET** `/appointments`

Retorna todos os agendamentos existentes.

#### ✔ Exemplo:

```bash
curl http://localhost:8003/appointments
```

#### ✔ Resposta esperada:

```json
[
  {
    "id": 1,
    "patient": "João Silva",
    "doctor_name": "Dr. Renato",
    "appointment_date": "2025-01-20T14:00:00"
  }
]
```

---

### **3. Criar Agendamento**

**POST** `/appointments`

Cria um novo agendamento para um paciente existente.

#### 📥 **Parâmetros**

| Nome             | Tipo                      | Obrigatório | Descrição               |
| ---------------- | ------------------------- | ----------- | ----------------------- |
| patient_id       | int                       | ✔           | ID do paciente          |
| doctor_name      | string                    | ✔           | Nome do médico          |
| appointment_date | string (YYYY-MM-DD HH:MM) | ✔           | Data e hora da consulta |

#### ✔ Exemplo válido:

```bash
curl -X POST "http://localhost:8003/appointments?patient_id=1&doctor_name=Dr.%20Pedro&appointment_date=2025-01-28%2010:30"
```

#### ✔ Resposta esperada:

```json
{
  "message": "Consulta agendada",
  "patient": "João Silva"
}
```

---
