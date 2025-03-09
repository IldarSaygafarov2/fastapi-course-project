FROM python:3.12


WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
COPY . .

CMD ["uvicorn", "main:main_app", "--host", "0.0.0.0", "--port", "4321"]

