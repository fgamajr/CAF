#!/usr/bin/env bash

set -euo pipefail

IMAGE="${ELASTIC_IMAGE:-docker.elastic.co/elasticsearch/elasticsearch:8.15.3}"
CONTAINER_NAME="${ELASTIC_CONTAINER_NAME:-caf-final-elasticsearch}"
PORT="${ELASTIC_PORT:-9200}"
DATA_DIR="${ELASTIC_DATA_DIR:-$(pwd)/.local/elasticsearch}"

mkdir -p "$DATA_DIR"

if ! command -v docker >/dev/null 2>&1; then
  echo "docker não encontrado no PATH" >&2
  exit 1
fi

if curl -fsS "http://localhost:${PORT}" >/dev/null 2>&1; then
  echo "Já existe um Elasticsearch respondendo em http://localhost:${PORT}"
  exit 0
fi

if ! docker info >/dev/null 2>&1; then
  echo "docker daemon indisponível" >&2
  exit 1
fi

if docker ps -a --format '{{.Names}}' | grep -qx "$CONTAINER_NAME"; then
  if docker ps --format '{{.Names}}' | grep -qx "$CONTAINER_NAME"; then
    echo "Elasticsearch já está em execução em http://localhost:${PORT}"
    exit 0
  fi
  docker start "$CONTAINER_NAME" >/dev/null
else
  docker run -d \
    --name "$CONTAINER_NAME" \
    -p "${PORT}:9200" \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    -e "ES_JAVA_OPTS=-Xms1g -Xmx1g" \
    -v "${DATA_DIR}:/usr/share/elasticsearch/data" \
    "$IMAGE" >/dev/null
fi

echo "Aguardando Elasticsearch responder..."
for _ in $(seq 1 60); do
  if curl -fsS "http://localhost:${PORT}" >/dev/null 2>&1; then
    echo "Elasticsearch disponível em http://localhost:${PORT}"
    exit 0
  fi
  sleep 2
done

echo "Elasticsearch não respondeu a tempo" >&2
exit 1
