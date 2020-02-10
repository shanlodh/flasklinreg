FROM python:3.6.6-slim

VOLUME ./:app/
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT python -m flasklinreg

# docker build -t flasklinreg .
# docker run
# docker save -o <path for generated tar file> <image name>
# docker load -i <path to image tar file>

