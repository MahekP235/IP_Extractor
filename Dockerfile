FROM python:3.9-slim
WORKDIR /app
#Copies entire project
COPY . .               
RUN pip install -r requirements.txt
#Critical for absolute imports
ENV PYTHONPATH=/app    