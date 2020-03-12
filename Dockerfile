FROM python:2.7.17

RUN apt-get update && apt-get install -y yui-compressor
COPY ./requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY ./ /app/

EXPOSE 8000
