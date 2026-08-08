FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./P2_Backend_House_Prediction

EXPOSE 8000

CMD ["sh", "-c", "uvicorn P2_Backend_House_Prediction.BE1_app:app --host 0.0.0.0 --port ${PORT:-8000}"]