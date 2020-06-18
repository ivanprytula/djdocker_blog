# How to start?

Clone repo. It's easy.  
Next.  
* Classic way:
  - in case you don't have *pipenv*: `$ pip install pipenv`
  - `$ pipenv install`
  - `$ ./manage.py migrate`
  - `$ ./manage.py runserver 8001`

* Docker way
   - `$ docker build -t <your_name>/<app_name>:<tag> .`
   - `$ docker run -d -t 8001:8001 <your_name>/<app_name>:<tag>`
   
* docker-compose way
   - `$ docker-compose build`
   - `$ docker-compose up`
   - `$ docker-compose down`




----
#### Credits
 - [Django documentation](https://docs.djangoproject.com/en/3.0/)
 - 'users' app & templates modified&adapted from [(c) 2020 Michael Herman](https://testdriven.io/blog/django-custom-user-model/)
 - [DjangoGirls tutorial](https://tutorial.djangogirls.org/en/)
 - [Cool Docker tutorial](https://docker-curriculum.com/)