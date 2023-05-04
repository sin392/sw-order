FROM mariadb:10.11 as base

RUN apt update \
    && apt install --no-install-recommends -y tzdata \
    && apt clean

RUN touch /var/log/mysql/mysqld.log