FROM python:3-alpine3.11
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 3000
CMD ["python", "./app.py"]