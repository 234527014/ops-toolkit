FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends iputils-ping \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY python/ /app/python/

ENTRYPOINT ["python", "python/ping_check.py"]
CMD ["--file", "hosts.txt"] 