FROM python:3

WORKDIR /usr/app

COPY requirements.txt .
COPY get_stream.py .
COPY app.py .

RUN pip3 install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
