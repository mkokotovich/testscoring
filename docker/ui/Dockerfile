FROM node:alpine
RUN yarn global add @angular/cli
RUN mkdir -p /usr/src/app/ui
WORKDIR /usr/src/app/ui
COPY ui/package.json package.json
COPY ui/yarn.lock yarn.lock
RUN yarn install
COPY ui .
RUN ng build --prod --build-optimizer
