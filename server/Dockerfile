FROM python:3
EXPOSE 5000


WORKDIR /usr/src/app

COPY requirements.txt ./

COPY app/resources ./db/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app/src/app.py" ]
