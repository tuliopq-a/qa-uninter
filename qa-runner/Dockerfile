FROM python:3.11-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /qa

# Copia apenas requirements e instala
COPY qa-runner/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia scripts
COPY qa-runner/run_pytest.sh .
COPY qa-runner/run_locust.sh .
RUN chmod +x run_pytest.sh run_locust.sh

# Copia testes e utilitários
COPY tests ./tests
COPY utils ./utils

# Comando padrão
CMD ["bash", "-c", "./run_pytest.sh && ./run_locust.sh", "--csv=/qa/logs/locust"]
