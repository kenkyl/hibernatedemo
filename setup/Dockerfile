FROM python:3
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["insert_data.py"]
ENTRYPOINT ["python3"]