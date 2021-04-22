FROM python:3.8
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin
RUN pip install -r requirements.txt
COPY . .
