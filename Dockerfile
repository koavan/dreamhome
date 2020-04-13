FROM python:3.6-slim-stretch

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /dreamhome

# Set the working directory to /dreamhome
WORKDIR /dreamhome

# Copy the current directory contents into the container at /music_service
ADD . /dreamhome/

RUN apt update

RUN apt install libpq-dev build-essential python-dev python3-psycopg2 -y

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "sh" ]