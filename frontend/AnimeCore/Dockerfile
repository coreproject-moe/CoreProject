FROM node:18-alpine as deploy-node

WORKDIR /app
COPY . .
RUN npm i
RUN 'npm build:node'

RUN rm -rf ./*
COPY --from=build /app/package.json .
COPY --from=build /app/build-node .
CMD ["node", "index.js"]
