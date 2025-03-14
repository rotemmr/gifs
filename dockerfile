#python compiler
FROM python:3.9-slim

#setting dir
WORKDIR /project

#cp files
COPY . /project/

#getting the git tag version --> ENV VAR
ARG VERSION
ENV VERSION=$VERSION

#requirements 
RUN pip install --no-cache-dir -r requirements.txt 

#port.5000 -> available (for flask)
EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["python", "app.py"]

