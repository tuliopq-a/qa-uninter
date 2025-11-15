#!/bin/bash

set -e

LOG_DIR="/qa/logs"
mkdir -p "$LOG_DIR"

echo "==== Esperando todos os serviços ficarem prontos para Pytest ===="

SERVICES=(
  "http://auth-service:8000/health"
  "http://patient-service:8000/health"
  "http://appointment-service:8000/health"
)

for SERVICE in "${SERVICES[@]}"; do
  echo "Aguardando $SERVICE..."
  while ! curl -s "$SERVICE" >/dev/null; do
    sleep 1
  done
done

echo "==== Running Pytest Functional Tests ===="
pytest tests/functional --disable-warnings --maxfail=1 | tee "$LOG_DIR/pytest.log"

echo "==== Pytest Completed ===="
