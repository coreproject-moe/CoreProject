FROM node:18-alpine as deploy-node

WORKDIR /app
COPY . .
RUN npm i
RUN npm run build:node

RUN mv package.json ./build
RUN ls
RUN cp -a ./build/ ./
CMD ["node", "index.js"]
