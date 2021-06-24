FROM node:15-alpine3.12 as builder

WORKDIR /usr/src/app

COPY --chown=node:node package*.json ./

RUN npm ci --only=production

#final
FROM node:lts-alpine3.12

ENV NODE_ENV production

USER node

WORKDIR /usr/src/app

COPY --chown=node:node --from=builder /usr/src/app/node_modules /usr/src/app/node_modules
COPY --chown=node:node . .

EXPOSE 8080

CMD ["npm", "start", "run"]