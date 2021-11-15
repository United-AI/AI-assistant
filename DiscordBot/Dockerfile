# syntax=docker/dockerfile:1
FROM node:16-alpine3.12
# RUN apk add --no-cache g++ make
WORKDIR /DiscordBot
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install
COPY . .
CMD ["node", "src/main.js"]
