# How to start?
* Classic way:
  - clone repo
  - in case you don't have *pipenv*: `$ pip install pipenv`
  - `$ pipenv install`
  - `$ ./manage.py migrate`
  - `$ ./manage.py runserver 8001`

* Docker way
 - clone repo
 - `$ docker build -t <your_name>/<app_name>:<tag> .`
 - `$ docker run -d -t 8001:8001 <your_name>/<app_name>:<tag>`



----
#### Credits
 - [Django documentation](https://docs.djangoproject.com/en/3.0/)
 - 'users' app & templates modified&adapted from [(c) 2020 Michael Herman](https://testdriven.io/blog/django-custom-user-model/)
 - [DjangoGirls tutorial](https://tutorial.djangogirls.org/en/)
 - [Cool Docker tutorial](https://docker-curriculum.com/)