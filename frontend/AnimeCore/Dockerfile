FROM node:18-alpine as deploy-node

WORKDIR /app
COPY . .
RUN npm i
RUN npm run build:node

RUN mv package.json ./build
RUN find . -maxdepth 1 ! -name 'build' -exec rm -rf "{}" \;
RUN cd ./build
CMD ["node", "build/index.js"]
