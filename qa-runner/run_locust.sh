#!/bin/bash

echo "==== Running Locust Load Tests ===="

# Autenticação
locust -f tests/performance/locust_auth.py --headless -u 50 -r 5 -t 30s \
 --host http://auth-service:8000 | tee /qa/locust_auth.log

# Pacientes
locust -f tests/performance/locust_patients.py --headless -u 50 -r 5 -t 30s \
 --host http://patient-service:8000 | tee /qa/locust_patients.log

# Agendamentos
locust -f tests/performance/locust_appointments.py --headless -u 50 -r 5 -t 30s \
 --host http://appointment-service:8000 | tee /qa/locust_appointments.log

echo "==== Locust Completed ===="
