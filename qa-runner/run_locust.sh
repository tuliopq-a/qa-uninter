#!/bin/bash
set -e

LOG_DIR="/qa/logs"
mkdir -p "$LOG_DIR"

echo "==== Esperando todos os serviços ficarem prontos para Locust ===="

SERVICES=(
  "http://auth-service:8000/health"
  "http://patient-service:8000/health"
  "http://appointment-service:8000/health"
)

for SERVICE in "${SERVICES[@]}"; do
  echo "Aguardando $SERVICE..."
  until curl -s "$SERVICE" >/dev/null; do
    sleep 1
  done
done

echo "==== Running Locust Load Tests ===="

# Função para rodar Locust com CSV e log de stdout
run_locust() {
  local FILE=$1
  local HOST=$2
  local LOG_PREFIX=$3
  local USERS=${4:-50}
  local SPAWN=${5:-5}
  local DURATION=${6:-30s}

  echo "==== Starting $FILE against $HOST ===="
  locust -f "$FILE" --headless -u "$USERS" -r "$SPAWN" -t "$DURATION" \
    --host "$HOST" \
    --csv="$LOG_DIR/$LOG_PREFIX" \
    --csv-full-history | tee "$LOG_DIR/$LOG_PREFIX.stdout.log"
  echo "==== Finished $FILE ===="
}

# Autenticação
run_locust tests/performance/locust_auth.py http://auth-service:8000 locust_auth

# Pacientes
run_locust tests/performance/locust_patients.py http://patient-service:8000 locust_patients

# Agendamentos
run_locust tests/performance/locust_appointments.py http://appointment-service:8000 locust_appointments

echo "==== Locust Completed ===="
