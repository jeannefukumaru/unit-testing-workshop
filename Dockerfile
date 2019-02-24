FROM python:3.6-slim

RUN apt-get update
RUN apt-get install -y curl git

WORKDIR /home/unit-testing-workshop

# COPY requirements.txt /home/unit-testing-workshop/requirements.txt
# RUN pip install -r requirements.txt

COPY . /home/unit-testing-workshop

CMD ["bash"]