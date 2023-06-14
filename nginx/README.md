# Ngnix notes

## Useful links
* [NGINX: Beginner’s Guide](https://nginx.org/en/docs/beginners_guide.html)
* [NGINX: Docker Official Build](https://hub.docker.com/_/nginx)
* [StackOverflow: How to start nginx via different port](https://stackoverflow.com/questions/10829402/how-to-start-nginx-via-different-portother-than-80)
* [Running the NGINX Server in a Docker Container](https://www.baeldung.com/linux/nginx-docker-container)

## Interacting with NGINX container

```shell
    $ docker exec -it nonbleedingedge-nginx-1 /bin/sh
```

The default ``nginx`` configuration file locations

* ``/etc/nginx/sites-available/default``
* ``/etc/nginx/conf.d/default.conf`` on ``nginx:mainline-alpine``

Copying content

```shell
    $ docker cp nonbleedingedge-nginx-1:/etc/nginx/conf.d/default.conf .
    $ docker cp default.conf nonbleedingedge-nginx-1:/etc/nginx/conf.d/default.conf
    # 
    $ docker cp foo.txt container_id:/foo.txt
    $ docker cp container_id:/foo.txt foo.txt
```
