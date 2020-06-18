# pull base image
FROM python:3.8-slim
LABEL maintainer="Ivan Prytula <ivanprytula87@gmail.com>"

# set environment variables
ENV PYTONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install system-wide dependencies for Python
RUN apt-get update \
    && apt-get install -qq -y \
        build-essential libpq-dev --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# set work directory for the app
WORKDIR /usr/src/app_djdocker_blog

# install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /usr/src/app_djdocker_blog/
RUN pipenv install --system

# copy project
COPY . /usr/src/app_djdocker_blog/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# tell the port number the container should expose
EXPOSE 8001

# run the command[s] == start app
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]