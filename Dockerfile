# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory to /app
RUN mkdir /app
RUN useradd docker && chown -R docker /app
VOLUME /app
WORKDIR /app

# COPY requirements to /app dir
COPY requirements.txt /app

USER root
# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# -- Install Pipenv:
# RUN apt install software-properties-common
# RUN add-apt-repository ppa:deadsnakes/ppa

# RUN apt update && apt upgrade -y && apt install python3.7 libffi-dev -y
# RUN curl --silent https://bootstrap.pypa.io/get-pip.py | python3.7

# # Backwards compatility.
# RUN rm -fr /usr/bin/python3 && ln /usr/bin/python3.7 /usr/bin/python3
RUN pip3 install pipenv

# RUN cd sample/flask && pipenv install && pipenv run uwsgi --ini WebAPI.ini  --wsgi-file wsgi.py --http :9090

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
# CMD ["pipenv", "run uwsgi --ini WebAPI.ini  --wsgi-file wsgi.py --http :9090"]
