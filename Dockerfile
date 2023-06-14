# https://www.docker.com/blog/how-to-use-the-apache-httpd-docker-official-image/
# https://hub.docker.com/r/bitnami/apache
FROM nginx:mainline-alpine
MAINTAINER Sjfke (Geoff Collis) <sjfke.pool.shark@hotmail.com>
ENV BUILDER_VERSION 1.0
ENV PORT=80
COPY ./_build/html/ /usr/share/nginx/html
EXPOSE ${PORT}