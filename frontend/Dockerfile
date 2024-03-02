FROM node:18.16.0-alpine3.17

WORKDIR /frontend/

COPY package.json .

COPY package-lock.json  .

RUN npm install

CMD npm start
