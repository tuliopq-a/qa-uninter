FROM python:3.11-slim

WORKDIR /qa

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY run_pytest.sh .
COPY run_locust.sh .
COPY .. /qa

RUN chmod +x run_pytest.sh
RUN chmod +x run_locust.sh

CMD ["bash", "-c", "./run_pytest.sh && ./run_locust.sh"]
