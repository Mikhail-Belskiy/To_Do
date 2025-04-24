FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml poetry.lock* /app/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root
COPY ./app /app/app

ENV DATABASE_URL=postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]