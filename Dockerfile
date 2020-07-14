FROM ubuntu:18.04

LABEL maintainer="vingtrung@gmail.com"

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip 

# We copy just the requirements.txt first to leverage Docker cache
# COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

# CMD ["flask", "run", "--host", "0.0.0.0"]
EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]

