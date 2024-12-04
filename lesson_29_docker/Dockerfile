FROM python:3.9-slim

RUN apt-get update && apt-get install -y netcat-openbsd

RUN python3 -m venv /venv

COPY requirements.txt .
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod -R 755 /app

ENV PATH="/venv/bin:$PATH"

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

ENV DATABASE_URL=postgres://username:password@postgres-db:5432/dbname

WORKDIR /app

EXPOSE 80

CMD ["./wait-for-it.sh", "postgres-db", "--", "pytest", "--maxfail=1", "--disable-warnings", "-v"]
