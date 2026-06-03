FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -i https://package-mirror.liara.ir/repository/pypi/simple --no-cache-dir --upgrade pip \
    && pip install -i https://package-mirror.liara.ir/repository/pypi/simple --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]