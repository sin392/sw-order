# base
FROM python:3.11 as base

RUN apt update \
    && apt install --no-install-recommends -y default-mysql-client \
    && apt clean

ARG USERNAME=user
ARG GROUPNAME=user
ARG UID=1000
ARG GID=1000
ARG APP_DIR=/home/app

RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME
USER user
WORKDIR $APP_DIR
ENV PYTHONPATH=$APP_DIR

# alembicは本番ではいらないかも
COPY requirements.txt .
RUN pip install -U & pip install --user -r requirements.txt

# development
FROM base as development

ENV APP_ENV=development
RUN pip install --user autopep8 flake8

CMD /bin/bash