#!/bin/bash
# wait-for-it.sh
host=$1
shift
until nc -z -v -w30 $host 5432
do
  echo "Waiting for database connection..."
  sleep 1
done
echo "Database is up"
exec "$@"

