# 🔒 Testes de Segurança – OWASP ZAP

Este diretório contém todos os artefatos relacionados aos testes de **segurança** realizados no ambiente SGHSS-QA.
O objetivo é identificar vulnerabilidades nos três microserviços (Autenticação, Pacientes e Agendamentos) usando técnicas automatizadas baseadas no **OWASP Top 10**.

---

# 🛠 Ferramenta utilizada

### **OWASP ZAP (Zed Attack Proxy)**

Um dos scanners de segurança mais utilizados no mundo para aplicações web.

Neste projeto foi utilizado:

* **Spider** (rastreamento de endpoints)
* **Active Scan** (ataques automatizados)
* **Passive Scan** (análise de respostas)
* **Relatório automatizado em HTML**

---

# 📄 Arquivos neste diretório

| Arquivo                       | Descrição                                                                          |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| `2025-11-16-ZAP-Report-.html` | Relatório completo gerado pelo ZAP, contendo todas as vulnerabilidades encontradas |
| `README.md`                   | Este documento com explicações, resumo dos resultados e orientações                |

> O relatório deve ser anexado no **PDF final** do seu trabalho como evidência dos testes de segurança realizados.

---


1. Abra o ZAP
2. Configure como proxy no postman e envie requisições do postman com proxy do zap para as apis
3. Vá botão direito na url do microserviço, adicione ao contexto
4. Clique para atacar ativamente


Ao final, exporte:
**Report → Generate HTML Report**

---

# 🧪 Escopo dos testes

Os seguintes componentes foram analisados:

| Serviço             | URL                                            | Testado                             |
| ------------------- | ---------------------------------------------- | ----------------------------------- |
| Auth Service        | [http://localhost:8001](http://localhost:8001) | ✔ SQL Injection, Param Tampering    |
| Patient Service     | [http://localhost:8002](http://localhost:8002) | ✔ Header Analysis, Input Validation |
| Appointment Service | [http://localhost:8003](http://localhost:8003) | ✔ Format String Injection           |

Todos os endpoints respondidos pelo spider foram avaliados automaticamente.

---

# 🚨 Resumo das vulnerabilidades detectadas

Com base no relatório `2025-11-16-ZAP-Report-.html`, o ZAP identificou:

---

## 🔥 **1 Vulnerabilidade Crítica — SQL Injection**

**Local:**

```
POST /login?cpf=...&password=...
```

**Evidência:**
Erro interno do servidor (500), provocado pela manipulação maliciosa da query SQL.


**Impacto:**
Acesso não autorizado, exposição de dados sensíveis.

---

## 🟠 **1 Vulnerabilidade Média — Format String Injection**

**Local:**

```
POST /appointments?doctor_name=ZAP%1...
```

**Evidência:**
Interpretação indevida de parâmetros e erro 500.


**Impacto:**
Possível execução de código ou manipulação da saída.

---

## 🟡 **1 Vulnerabilidade Baixa — Falta de Header de Segurança**

**Local:**

```
GET /health
```

**Header ausente:**
`X-Content-Type-Options`


**Impacto:**
Risco reduzido, mas recomendado mitigar.

---

## 🔵 **1 Informativa — Exposição de senha em querystring**

**Local:**

```
POST /login?password=123
```



**Impacto:**
A senha fica registrada em logs, histórico, proxy etc.
Boa para demonstrar falhas de design em APIs.

---

# 🧯 Recomendações de mitigação

### ✔ SQL Injection

* Usar sempre **queries parametrizadas** (já existe no projeto)
* Escapar entradas de usuário
* Implementar validação forte no backend

### ✔ Format String Injection

* Sanitizar entradas do tipo string
* Remover caracteres de formatação especial

### ✔ Headers ausentes

Adicionar no FastAPI:

```python
from fastapi.responses import Response

Response(headers={"X-Content-Type-Options": "nosniff"})
```

### ✔ Senha na URL

Substituir parâmetros GET por **POST com JSON**.

---
