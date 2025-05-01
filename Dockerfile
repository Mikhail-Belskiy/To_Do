FROM python:3.12-slim

WORKDIR /app

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY requirements.txt /app/

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY ./app /app/app

ENV DATABASE_URL=postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
