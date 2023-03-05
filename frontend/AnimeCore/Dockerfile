FROM node:18-alpine as deploy-node

WORKDIR /app
COPY . .
RUN npm i
RUN npm run build:node

RUN rm -rf ./*
COPY --from=build /app/package.json .
COPY --from=build /app/build .
CMD ["node", "index.js"]
