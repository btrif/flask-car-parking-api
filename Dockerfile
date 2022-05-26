# init a base image (Alpine is small Linux distro)
FROM python:3.9-alpine
#FROM alpine:latest

#  MUST Install Python 3 && upgrade pip
# RUN apk add --no-cache python3   && pip install --upgrade pip
RUN pip install --upgrade pip

# define the present working directory
WORKDIR /oracle-car-parking

# copy the contents of current folder "." into the working dir of the docker image
ADD . /oracle-car-parking

# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt

# Environment variables
ENV FLASK_APP="app.py"

# define the command to start the container
CMD ["python", "app.py"]