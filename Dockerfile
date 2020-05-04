FROM python:3.6-slim-stretch

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /src

# Set the working directory to /src
WORKDIR /src

# Install necessary packages
RUN apt-get update && apt-get install -y libpq-dev \
build-essential \
python-dev \
python3-psycopg2 \
&& rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /tmp
ADD requirements.txt /tmp

# Install any needed packages specified in requirements.txt
RUN pip3 install -r /tmp/requirements.txt

EXPOSE 8000

CMD [ "sh" ]