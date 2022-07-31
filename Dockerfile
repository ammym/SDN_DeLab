FROM python:3.11.0b5-alpine3.16
WORKDIR /DeLab
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python","script.py"]


