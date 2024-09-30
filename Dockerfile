FROM alpine:3.20.3

RUN apk add --no-cache python3

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./app.py" ]
