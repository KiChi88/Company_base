FROM python:3.6

RUN mkdir -p /home/company_base

WORKDIR /home/company_base

COPY requirements.txt ./   
RUN pip install --no-cache-dir -r requirements.txt

COPY . .