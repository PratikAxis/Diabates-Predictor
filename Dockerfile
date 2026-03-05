FROM python:3.10.19-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && / pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "src/main.py"]