FROM python:3.9-slim

RUN pip install mlflow

CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000"]
# This Dockerfile sets up a minimal environment for running an MLflow server.
# It uses a slim Python 3.9 image, installs MLflow, and starts the server on port 5000.