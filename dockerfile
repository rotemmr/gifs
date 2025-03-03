#python compiler
FROM python:3.9-slim

#setting dir
WORKDIR /project

#cp files
COPY . /project/

#requirements 
RUN pip install --no-cache-dir -r requirements.txt && \
    apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

#port.5000 -> available (for flask)
EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["python", "app.py"]

