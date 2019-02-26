FROM python:3.6-slim

RUN apt-get update \
  && apt-get install -y curl git

RUN git config --global credential.helper 'cache --timeout=36000'

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

ARG user
RUN useradd ${user:-root} -g root || true
USER ${user:-root}

EXPOSE 8888

CMD ["bash"]