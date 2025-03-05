#python compiler
FROM python:3.9-slim

# Install MySQL client to interact with the database
RUN apt-get update && apt-get install -y mysql-client

#setting dir
WORKDIR /project

#cp files
COPY . /project/

#getting the git tag version --> ENV VAR
ARG VERSION
ENV VERSION=$VERSION

#vars from github secrets
ARG DB_HOST
ARG DB_USER
ARG DB_PASSWORD
ARG DB_NAME

ENV DB_HOST=${DB_HOST}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_NAME=${DB_NAME}

#requirements 
RUN pip install --no-cache-dir -r requirements.txt 

#port.5000 -> available (for flask)
EXPOSE 5000

ENV FLASK_APP=app.py

#Variables from Github Secrets


CMD ["python", "app.py"]

