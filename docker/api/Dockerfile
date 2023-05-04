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

WORKDIR $APP_DIR
ENV PYTHONPATH=$APP_DIR

# alembicは本番ではいらないかも
COPY requirements.txt .
RUN pip install -U & pip install -r requirements.txt

RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME
USER $USERNAME

# development
FROM base as development
COPY --from=base /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages/
USER root
RUN apt install --no-install-recommends -y vim \
    && pip install autopep8 flake8

USER $USERNAME
ENV APP_ENV=development

CMD /bin/bash