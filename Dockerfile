# Install (or build) dependencies
FROM python:3 AS builder

COPY requirements.txt .

RUN pip install --user -r requirements.txt

# Build image
FROM python:3-slim

WORKDIR /usr/app
COPY --from=builder /root/.local /root/.local
COPY get_stream.py .
COPY app.py .

EXPOSE 8000
ENV PATH=/root/.local/bin:$PATH
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
