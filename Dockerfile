FROM python:3-slim

LABEL maintainer="andrew@andrewherrington.com"
LABEL description="Plangrid homework"

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /requirements.txt && \
    rm -f /requirements.txt

COPY app.py /app.py
COPY config.py /config.py
COPY templates/ /templates

EXPOSE 8000
ENV PORT 8000
ENV LOGLEVEL INFO

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT --workers 2 --log-level $LOGLEVEL app:app"]
