FROM python:3.8.12-alpine

WORKDIR /app
COPY . .

# install requirements
RUN apk add --no-cache --virtual build-deps gcc musl-dev libffi-dev
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir -r requirements.txt
RUN apk del build-deps

WORKDIR /app/workdir
CMD [ "python", "../src/app.py" ]
