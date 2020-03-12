FROM python:2.7.17

RUN apt-get update && apt-get install -y yui-compressor
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY ./ /app/
RUN chown -R 1000:1000 /app
USER 1000
EXPOSE 8000
WORKDIR /app
