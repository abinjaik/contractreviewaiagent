docker build -t mlflow-server .
docker run -p 5000:5000 mlflow-server